from django.db import models



class User(models.Model):
    """
    name: User
    author: miamoyoualeu5@gmail.com
    description: User model to store user information
    """
    username = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.username


class Category(models.Model):
    """
    name: Category
    author: miamoyoualeu5@gmail.com
    description: Category model to store product categories
    """
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Product(models.Model):
    """
    name: Product
    author: miamoyoualeu5@gmail.com
    description: Product model to store product information
    """
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    discount_price = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    cover_image = models.ImageField(upload_to='products')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Basket(models.Model):
    """
    name: Basket
    author: miamoyoualeu5@gmail.com
    description: Basket model to store user baskets
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='BasketProduct')
    total_price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"{self.user}'s basket"


class BasketProduct(models.Model):
    """
    name: BasketProduct
    author: miamoyoualeu5@gmail.com
    description: BasketProduct model to represent the many-to-many relationship between Basket and Product
    """
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()


class Order(models.Model):
    """
    name: Order
    author: miamoyoualeu5@gmail.com
    description: Order model to store user orders
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='OrderProduct')
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=False)
    delivery_address = models.TextField()

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f"{self.user}'s order"


class OrderProduct(models.Model):
    """
    name: OrderProduct
    author: miamoyoualeu5@gmail.com
    description: OrderProduct model to represent the many-to-many relationship between Order and Product
    """
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f'{self.quantity} x {self.product.name}'

class Payment(models.Model):
    """
    name: Payment
    author: miamoyoualeu5@gmail.com
    description: Payment model to store payment information
    """
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)



