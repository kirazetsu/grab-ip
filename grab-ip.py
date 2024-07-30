import random

# 隨機 IP 地址產生器，按使用者輸入數量來產生 IP 地址，並儲存到 ip-list.txt 檔案
# lu recode lu noob anjeng | thx to Clan_X12 | Vernest Team | Manusia Biasa Team
# author : Mr.Crifty / KIRAZETSU

def minta_jumlah_result():
    while True:
        try:
            jumlah = int(input("Lí beh chia̍h sióng hāi? "))  # 問使用者需要幾個結果
            if jumlah > 0:
                return jumlah
            else:
                print("Chia̍h sióng hāi bē sī tī 0 kap ūn. Tâi-á lâi.")  # 輸入無效，請再試一次
        except ValueError:
            print("Lí ê sióng hāi bō tsì. Tâi-á lâi.")  # 輸入無效，請再試一次

def generate_ip():
    # 產生隨機 IP 地址
    return '.'.join(str(random.randint(0, 255)) for _ in range(4))

def kumpulkan_ip(jumlah):
    ip_list = []  # 建立一個空的列表來儲存 IP 地址
    print(f"Khì sióng {jumlah} ê IP address:")
    for i in range(jumlah):
        ip = generate_ip()  # 產生隨機 IP
        ip_list.append(ip)
    return ip_list

def simpan_ip(ip_list):
    # 儲存 IP 地址列表到 ip-list.txt 檔案
    with open("ip-list.txt", "w") as file:
        for ip in ip_list:
            file.write(ip + "\n")
    print("IP list tsò sī sùb-îng tī 'ip-list.txt'!")  # 提示儲存成功

def main():
    jumlah = minta_jumlah_result()
    ip_list = kumpulkan_ip(jumlah)
    simpan_ip(ip_list)  # 儲存 IP 列表到檔案
    print("\nIP sī tsò khì bô kap hō͘-lo̍h:")
    for i, ip in enumerate(ip_list, start=1):
        print(f"IP ke-{i}: {ip}")

if __name__ == "__main__":
    main()
