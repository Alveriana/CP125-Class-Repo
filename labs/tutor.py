"""def generate_emails(employees):
    emails = []

    for item in employees:
        first_name = item["first"].lower()
        last_name = item["last"].lower()

        email = first_name + "." + last_name + "@company.com"
        emails.append(email)

    return emails"""

"""def find_high_value_transactions(transactions, threshold):
    ids = []
    for item in transactions:
        if item["amount"] > threshold:
            ids.append(item["amount"])
    return ids"""

'''def archive_inactive_users(users):
    inactive_ids = []

    for user in users:
        if user["status"] == "inactive":
            inactive_ids.append(user["user_id"])

    return inactive_ids

user_table = [
    {"user_id": "U001", "name": "Ali", "status": "active", "login_count": 45},
    {"user_id": "U002", "name": "Sara", "status": "inactive", "login_count": 2},
    {"user_id": "U003", "name": "John", "status": "active", "login_count": 30},
    {"user_id": "U004", "name": "Maya", "status": "inactive", "login_count": 0}
]

print(archive_inactive_users(user_table))'''

'''def merge_sales_data(region1_sales, region2_sales):
    merged = {}
    for record in region1_sales:
        merged[record["transaction_id"]] = record

    for record in region2_sales:
        tid = record["transaction_id"]

        if tid not in merged:
            merged[tid] = record
        else:
            if record["amount"] > merged[tid]["amount"]:
                merged[tid] = record

    return list(merged.values())

region1_sales = [
    {"transaction_id": "T001", "product": "Laptop", "amount": 1200.00, "date": "2024-01-15"},
    {"transaction_id": "T002", "product": "Mouse", "amount": 25.00, "date": "2024-01-16"},
    {"transaction_id": "T003", "product": "Keyboard", "amount": 75.00, "date": "2024-01-17"}
]

region2_sales = [
    {"transaction_id": "T002", "product": "Mouse", "amount": 30.00, "date": "2024-01-16"},
    {"transaction_id": "T004", "product": "Monitor", "amount": 350.00, "date": "2024-01-18"}
]

print(merge_sales_data(region1_sales, region2_sales))'''

"""def group_students_by_course(enrollments):
    courses = {}

    for record in enrollments:
        course = record["course_code"]
        student = record["student_name"]

        if course not in courses:
            courses[course] = []

        courses[course].append(student)

    return courses

enrollments = [
    {"student_id": "S001", "student_name": "Ali", "course_code": "CP125", "semester": "Fall2024"},
    {"student_id": "S002", "student_name": "Sara", "course_code": "CP126", "semester": "Fall2024"},
    {"student_id": "S003", "student_name": "John", "course_code": "CP125", "semester": "Fall2024"},
    {"student_id": "S004", "student_name": "Maya", "course_code": "CP126", "semester": "Fall2024"},
    {"student_id": "S005", "student_name": "Bob", "course_code": "CP125", "semester": "Fall2024"}
]

print(group_students_by_course(enrollments))"""

'''def find_overdue_users(loans, current_date):
    overdue_list = []
    for item in loans:
        due_date = loans[item]
        for dates in due_date:
            if dates > current_date:
                overdue_list.append(item)
                break # no need to check other books for this user
    return overdue_list

loans = {
    "ali@email.com": [45, 50, 55],
    "sara@email.com": [40, 42]
}
current_date = 48
print(find_overdue_users(loans, current_date))'''

'''def apply_discount(cart, discount_code, codes):
    total = 0
    for item in cart:
        amount = item["price"] * item["qty"]
        total += amount

    if discount_code in codes:
        code_info = codes[discount_code]
        min_purchase = code_info["min_purchase"]
        discount_percent = code_info["discount"]

    if total >= min_purchase:
        discount_amount = total * discount_percent
        total -= discount_amount
    return total

cart = [
    {"name": "Laptop", "price": 1000, "qty": 1},
    {"name": "Mouse", "price": 50, "qty": 2}
]
discount_code = "SAVE10"
codes = {
    "SAVE10": {"min_purchase": 500, "discount": 0.10},
    "SAVE20": {"min_purchase": 2000, "discount": 0.20}
}
print(apply_discount(cart, discount_code, codes))
print()'''

'''def remove_consecutive_artists(playlist, song_artists):
    if not playlist:
        return []

    filtered_playlist = [playlist[0]]  # always keep the first song
    last_artist = song_artists[playlist[0]]

    for song_id in playlist[1:]:
        current_artist = song_artists[song_id]
        if current_artist != last_artist:
            filtered_playlist.append(song_id)
            last_artist = current_artist

    return filtered_playlist

playlist = [101, 102, 103, 104, 105]
song_artists = {
    101: "Taylor Swift",
    102: "Taylor Swift",
    103: "Ed Sheeran",
    104: "Taylor Swift",
    105: "Ed Sheeran"
}
print(remove_consecutive_artists(playlist, song_artists))
print()'''

def filter_products(products, preferred_categories, blocked_brands):
    '''list_product = []
    for product_name, info in products.items():
        category = info["category"]
        brand = info["brand"]
        if category in preferred_categories and brand not in blocked_brands:
            list_product.append(product_name)
    return list_product'''

    list_product = []
    for item in products:
        category = products[item]["category"]
        brand = products[item]["brand"]
        if category in preferred_categories and brand not in blocked_brands:
            list_product.append(item)
    return list_product

products = {
    "iPhone": {"category": "Electronics", "brand": "Apple"},
    "Galaxy": {"category": "Electronics", "brand": "Samsung"},
    "Shirt": {"category": "Clothing", "brand": "Nike"}
}
preferred_categories = {"Electronics"}
blocked_brands = {"Apple"}
print(filter_products(products, preferred_categories, blocked_brands))