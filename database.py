import sqlite3



class Database:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    # WORK WITH CATEGORIES
    def get_categories(self):       # get all categories
        categories = self.cursor.execute(
            "SELECT id, category_name FROM categories;"
        )
        return categories.fetchall()

    def add_category(self, new_category):
        try:
            self.cursor.execute(
                "INSERT INTO categories (category_name) VALUES(?);",
                (new_category,)
            )
            self.conn.commit()
            return True
        except:
            return False

    def rename_category(self, old_name, new_name):
        try:
            self.cursor.execute(
                "UPDATE categories SET category_name=? WHERE category_name=?;",
                (new_name, old_name)
            )
            self.conn.commit()
            return True
        except:
            return False

    def delete_category(self, name):
        try:
            self.cursor.execute(
                "DELETE FROM categories WHERE category_name=?;",
                (name,)
            )
            self.conn.commit()
            return True
        except:
            return False

    def check_category_exists(self, name):
        lst = self.cursor.execute(
            f"SELECT * FROM categories WHERE category_name=?",
            (name,)
        ).fetchall()
        if not lst:
            return True
        else:
            return False




    def add_product(self, title, text, image, price, phone, cat_id, u_id):
        # try:
            if cat_id is None:
                cat_id = 0
            self.cursor.execute(
                f"INSERT INTO products (product_title, "
                f"product_text, "
                f"product_image, "
                f"product_price, "
                f"product_phone, "
                f"product_category, "
                f"product_owner)"
                f"VALUES (?, ?, ?, ?, ?, ?, ?)",
                (title, text, image, price, phone, cat_id, u_id)
            )
            self.conn.commit()
            return True
        # except:
        #     print("Error while adding product")
        #     return False

    def get_my_last_product(self, u_id):
        product = self.cursor.execute(
            f"SELECT id, product_title, product_text, product_image, product_price, product_phone FROM products WHERE product_owner=? ORDER BY id DESC LIMIT 1",
            (u_id,)
        )
        return product.fetchone()




    def update_product(self, product_id, title=None, text=None, image=None, price=None, phone=None, cat_id=None):
        try:
            update_values = []
            update_query = "UPDATE products SET"

            if title is not None:
                update_values.append(title)
                update_query += " product_title = ?,"

            if text is not None:
                update_values.append(text)
                update_query += " product_text = ?,"

            if image is not None:
                update_values.append(image)
                update_query += " product_image = ?,"

            if price is not None:
                update_values.append(price)
                update_query += " product_price = ?,"

            if phone is not None:
                update_values.append(phone)
                update_query += " product_phone = ?,"

            if cat_id is not None:
                update_values.append(cat_id)
                update_query += " product_cat_id= ?,"

            update_query += update_query.rstrip(',')

            update_query += " WHERE product_id = ?"
            update_values.append(product_id)
            self.cursor.execute(update_query, tuple(update_values))
            self.conn.commit()
            return True
        except:
            return False

    def get_products_by_category(self, category_id):
        products = []
        self.cursor.execute(
            "SELECT * FROM products WHERE product_category = ?", (category_id,)
        )
        rows = self.cursor.fetchall()
        for row in rows:
            product = {
                'id': row['id'],
                'title': row['title'],
                'text': row['text'],
                'image': row['image'],
                'price': row['price'],
                'phone': row['phone'],
                'category': row['category'],
                'owner': row['owner']
            }
            products.append(product)
        return products

    def delete_product(self, name):
        try:
            self.cursor.execute(
                "DELETE FROM products WHERE product_name=?;",
                (name,)
            )
            self.conn.commit()
            return True
        except:
            return False


    def get_products(self):
        products = self.cursor.execute(
            "SELECT id, product_title FROM products WHERE product_owner = 1547040457;"
        )
        return products.fetchall()