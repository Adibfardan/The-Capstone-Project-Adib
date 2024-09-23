# Global variables
customers = {}  # Dictionary to store customer ID as key and a tuple of (name, package) as value
packages = {
    "Hemat": {"price": 26000000, "stock": 10},     # Price in rupiah, stock availability
    "Executive": {"price": 35000000, "stock": 10},
    "Akhir Tahun": {"price": 32000000, "stock": 10},
    "Maulid":{"price":28000000,"stock":10},
    "Awal Tahun":{"price":34000000,"stock":10},
    "Ramadhan":{"price":40000000,"stock":10}
}
customer_id_counter = 1  # Counter for generating unique customer IDs

def generate_customer_id():
    global customer_id_counter
    customer_id = f"{customer_id_counter}"
    customer_id_counter += 1
    return customer_id

def input_customer_data():
    global customers, packages
    name = input("Masukkan Nama Jamaah: ")
    package = input("Masukkan Paket Pilihan (Hemat, Executive, Akhir Tahun, Maulid, Awal Tahun, Ramadhan): ")
    
    if package not in packages:
        print(f"Paket Umrah '{package}' Tidak Tersedia.")
        return
    
    # Check package stock
    if packages[package]['stock'] <= 0:
        print(f"Maaf, stok paket {package} habis.")
        return
    
    customer_id = generate_customer_id()
    customers[customer_id] = (name, package)
    
    # Decrease stock
    packages[package]['stock'] -= 1
    
    print(f"Jamaah {name} dengan ID {customer_id} sudah terdaftar untuk Paket Umrah {package} dengan harga Rp{packages[package]['price']}. Stok tersisa: {packages[package]['stock']}")

def list_customers():
    if not customers:
        print("Tidak Ada Data Jamaah.")
        return
    print("Daftar Jamaah:")
    for customer_id, (name, package) in customers.items():
        print(f"ID Jamaah: {customer_id}, Nama Jamaah: {name}, Paket Umrah: {package}, Harga: Rp{packages[package]['price']}")

def list_packages():
    print("Daftar Paket Umrah & Harga: ")
    for package, details in packages.items():
        print(f"{package}: Rp{details['price']}, Stok: {details['stock']}")

def update_package():
    customer_id = input("Masukkan ID Jamaah untuk mengganti pilihan paket: ")
    new_package = input("Masukkan Pilihan Paket Umrah Baru (Hemat, Executive, Akhir Tahun, Maulid, Awal Tahun, Ramadhan): ")
    
    if customer_id not in customers:
        print(f"ID Jamaah {customer_id} belum terdaftar.")
        return
    if new_package not in packages:
        print(f"Paket Umrah {new_package} tidak tersedia.")
        return
    if packages[new_package]['stock'] <= 0:
        print(f"Maaf, stok paket {new_package} habis.")
        return
    
    # Increase stock of the old package
    old_package = customers[customer_id][1]
    packages[old_package]['stock'] += 1

    # Decrease stock of the new package
    packages[new_package]['stock'] -= 1
    
    # Update customer package, directly accessing name
    name = customers[customer_id][0]
    customers[customer_id] = (name, new_package)
    
    print(f"ID Jamaah {customer_id} mengganti paket ke Paket Umrah {new_package} dengan harga Rp{packages[new_package]['price']}. Stok tersisa: {packages[new_package]['stock']}")

def cancel_registration():
    customer_id = input("Masukkan ID untuk pembatalan pendaftaran: ")
    
    if customer_id not in customers:
        print(f"ID Jamaah {customer_id} tidak terdaftar.")
        return
    
    # Directly access the package (index 1) without using `_`
    package = customers[customer_id][1]
    
    # Increase stock of the canceled package
    packages[package]['stock'] += 1
    
    del customers[customer_id]
    print(f"Pendaftaran Jamaah dengan ID {customer_id} berhasil dibatalkan.")

def filter_packages_by_price():
    min_price = int(input("Masukkan harga minimum: "))
    max_price = int(input("Masukkan harga maksimum: "))
    
    filtered_packages = {pkg: details for pkg, details in packages.items() if min_price <= details['price'] <= max_price}
    
    if not filtered_packages:
        print(f"Tidak ada paket dengan harga di antara Rp{min_price} dan Rp{max_price}.")
    else:
        print(f"Paket Umrah dengan harga di antara Rp{min_price} dan Rp{max_price}:")
        for package, details in filtered_packages.items():
            print(f"{package}: Rp{details['price']}, Stok: {details['stock']}")

def list_packages_sorted():
    sorted_packages = sorted(packages.items(), key=lambda x: x[1]['price'])
    print("Daftar Paket Umrah (Termurah ke Termahal):")
    for package, details in sorted_packages:
        print(f"{package}: Rp{details['price']}, Stok: {details['stock']}")

def main_menu():
    while True:
        print("\n1. Pendaftaran Jamaah")
        print("2. Daftar Jamaah")
        print("3. Daftar Paket Umrah")
        print("4. Pergantian Paket Umrah")
        print("5. Pembatalan Pendaftaran")
        print("6. Filter Paket Umrah Berdasarkan Harga")
        print("7. Urutkan Paket Umrah Berdasarkan Harga")
        print("8. Keluar")

        choice = input("Masukkan Pilihan Anda (1-8): ")
        
        if choice == '1':
            input_customer_data()
        elif choice == '2':
            list_customers()
        elif choice == '3':
            list_packages()
        elif choice == '4':
            update_package()
        elif choice == '5':
            cancel_registration()
        elif choice == '6':
            filter_packages_by_price()
        elif choice == '7':
            list_packages_sorted()
        elif choice == '8':
            print("Keluar...")
            break
        else:
            print("Input salah, masukkan angka 1-8.")
        
        # Ask if user wants to return to main menu or exit
        if choice != '8':
            input("Tekan Enter untuk kembali ke menu utama...")

# Main execution
if __name__ == "__main__":
    main_menu()
