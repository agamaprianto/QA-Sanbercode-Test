import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Variable Register
# Name     : agam123
# Email    : agam@gmail.com
# Password : agam123



class TestRegister(unittest.TestCase): 

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_a_success_register(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("http://barru.pythonanywhere.com/daftar") # buka situs
        time.sleep(3)
        browser.find_element(By.ID,"signUp").click() # klik tombol sign up
        time.sleep(1)
        browser.find_element(By.ID,"name_register").send_keys("agam123") # isi username
        time.sleep(1)
        browser.find_element(By.ID,"email_register").send_keys("agam@gmail.com") # isi email
        time.sleep(1)
        browser.find_element(By.ID,"password_register").send_keys("agam123") # isi password
        time.sleep(1)
        browser.find_element(By.ID,"signup_register").click() # klik tombol sign up
        time.sleep(1)

        # validasi
        response_data = browser.find_element(By.ID,"swal2-title").text
        response_message = browser.find_element(By.ID,"swal2-content").text

        self.assertIn('berhasil', response_data)
        self.assertEqual(response_message, 'created user!')

    def test_b_failed_register_with_invalid_email(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("http://barru.pythonanywhere.com/daftar") # buka situs
        time.sleep(3)
        browser.find_element(By.ID,"signUp").click() # klik tombol sign up
        time.sleep(1)
        browser.find_element(By.ID,"name_register").send_keys("agam123") # isi username
        time.sleep(1)
        browser.find_element(By.ID,"email_register").send_keys("agam@gmail") # isi email
        time.sleep(1)
        browser.find_element(By.ID,"password_register").send_keys("agam123") # isi password
        time.sleep(1)
        browser.find_element(By.ID,"signup_register").click() # klik tombol sign up
        time.sleep(1)

        # validasi
        response_data = browser.find_element(By.ID,"swal2-title").text
        response_message = browser.find_element(By.ID,"swal2-content").text

        self.assertIn('Email tidak valid', response_data)
        self.assertEqual(response_message, 'Cek kembali email anda')

    def test_c_failed_register_with_empty_name(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("http://barru.pythonanywhere.com/daftar") # buka situs
        time.sleep(3)
        browser.find_element(By.ID,"signUp").click() # klik tombol sign up
        time.sleep(1)
        browser.find_element(By.ID,"name_register").send_keys("") # isi username
        time.sleep(1)
        browser.find_element(By.ID,"email_register").send_keys("agam@gmail.com") # isi email
        time.sleep(1)
        browser.find_element(By.ID,"password_register").send_keys("agam123") # isi password
        time.sleep(1)
        browser.find_element(By.ID,"signup_register").click() # klik tombol sign up
        time.sleep(1)

        # validasi
        response_data = browser.find_element(By.ID,"swal2-title").text
        response_message = browser.find_element(By.ID,"swal2-content").text

        self.assertIn('Email/Username/Password tidak boleh kosong', response_data)
        self.assertEqual(response_message, 'Gagal Registrasi')

    def test_d_failed_register_with_empty_email(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("http://barru.pythonanywhere.com/daftar") # buka situs
        time.sleep(3)
        browser.find_element(By.ID,"signUp").click() # klik tombol sign up
        time.sleep(1)
        browser.find_element(By.ID,"name_register").send_keys("agam123") # isi username
        time.sleep(1)
        browser.find_element(By.ID,"email_register").send_keys("") # isi email
        time.sleep(1)
        browser.find_element(By.ID,"password_register").send_keys("agam123") # isi password
        time.sleep(1)
        browser.find_element(By.ID,"signup_register").click() # klik tombol sign up
        time.sleep(1)

        # validasi
        response_data = browser.find_element(By.ID,"swal2-title").text
        response_message = browser.find_element(By.ID,"swal2-content").text

        self.assertIn('Email/Username/Password tidak boleh kosong', response_data)
        self.assertEqual(response_message, 'Gagal Registrasi')

    def test_e_failed_register_with_empty_password(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("http://barru.pythonanywhere.com/daftar") # buka situs
        time.sleep(3)
        browser.find_element(By.ID,"signUp").click() # klik tombol sign up
        time.sleep(1)
        browser.find_element(By.ID,"name_register").send_keys("agam123") # isi username
        time.sleep(1)
        browser.find_element(By.ID,"email_register").send_keys("agam@gmail.com") # isi email
        time.sleep(1)
        browser.find_element(By.ID,"password_register").send_keys("") # isi password
        time.sleep(1)
        browser.find_element(By.ID,"signup_register").click() # klik tombol sign up
        time.sleep(1)

        # validasi
        response_data = browser.find_element(By.ID,"swal2-title").text
        response_message = browser.find_element(By.ID,"swal2-content").text

        self.assertIn('Email/Username/Password tidak boleh kosong', response_data)
        self.assertEqual(response_message, 'Gagal Registrasi')

    def test_f_failed_register_with_special_name_character(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("http://barru.pythonanywhere.com/daftar") # buka situs
        time.sleep(3)
        browser.find_element(By.ID,"signUp").click() # klik tombol sign up
        time.sleep(1)
        browser.find_element(By.ID,"name_register").send_keys("agam123@@") # isi username
        time.sleep(1)
        browser.find_element(By.ID,"email_register").send_keys("agam@gmail.com") # isi email
        time.sleep(1)
        browser.find_element(By.ID,"password_register").send_keys("agam123") # isi password
        time.sleep(1)
        browser.find_element(By.ID,"signup_register").click() # klik tombol sign up
        time.sleep(1)

        # validasi
        response_data = browser.find_element(By.ID,"swal2-title").text
        response_message = browser.find_element(By.ID,"swal2-content").text

        self.assertIn('Nama atau password tidak valid', response_data)
        self.assertEqual(response_message, 'Tidak boleh mengandung symbol')

    def test_g_failed_register_with_special_email_character(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("http://barru.pythonanywhere.com/daftar") # buka situs
        time.sleep(3)
        browser.find_element(By.ID,"signUp").click() # klik tombol sign up
        time.sleep(1)
        browser.find_element(By.ID,"name_register").send_keys("agam123") # isi username
        time.sleep(1)
        browser.find_element(By.ID,"email_register").send_keys("ag!am@gmail.com") # isi email
        time.sleep(1)
        browser.find_element(By.ID,"password_register").send_keys("agam123") # isi password
        time.sleep(1)
        browser.find_element(By.ID,"signup_register").click() # klik tombol sign up
        time.sleep(1)

        # validasi
        response_data = browser.find_element(By.ID,"swal2-title").text
        response_message = browser.find_element(By.ID,"swal2-content").text

        self.assertIn('Nama atau password tidak valid', response_data)
        self.assertEqual(response_message, 'Tidak boleh mengandung symbol')

    def test_h_failed_register_with_special_password_character(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("http://barru.pythonanywhere.com/daftar") # buka situs
        time.sleep(3)
        browser.find_element(By.ID,"signUp").click() # klik tombol sign up
        time.sleep(1)
        browser.find_element(By.ID,"name_register").send_keys("agam123") # isi username
        time.sleep(1)
        browser.find_element(By.ID,"email_register").send_keys("agam@gmail.com") # isi email
        time.sleep(1)
        browser.find_element(By.ID,"password_register").send_keys("agam123@") # isi password
        time.sleep(1)
        browser.find_element(By.ID,"signup_register").click() # klik tombol sign up
        time.sleep(1)

        # validasi
        response_data = browser.find_element(By.ID,"swal2-title").text
        response_message = browser.find_element(By.ID,"swal2-content").text

        self.assertIn('Nama atau password tidak valid', response_data)
        self.assertEqual(response_message, 'Tidak boleh mengandung symbol')

    def tearDown(self): 
        self.browser.close() 


class TestLogin(unittest.TestCase): 

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_a_success_login(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("http://barru.pythonanywhere.com/daftar") # buka situs
        time.sleep(3)
        browser.find_element(By.ID,"email").send_keys("agam@gmail.com") # isi email
        time.sleep(1)
        browser.find_element(By.ID,"password").send_keys("agam123") # isi password
        time.sleep(1)
        browser.find_element(By.ID,"signin_login").click() # klik tombol sign in
        time.sleep(1)

        # validasi
        response_data = browser.find_element(By.ID,"swal2-title").text
        response_message = browser.find_element(By.ID,"swal2-content").text

        self.assertIn('Welcome', response_data)
        self.assertEqual(response_message, 'Anda Berhasil Login')

    def test_b_failed_login_with_dot_trick_email(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("http://barru.pythonanywhere.com/daftar") # buka situs
        time.sleep(3)
        browser.find_element(By.ID,"email").send_keys("ag.am@gmail.com") # isi email
        time.sleep(1)
        browser.find_element(By.ID,"password").send_keys("agam123") # isi password
        time.sleep(1)
        browser.find_element(By.ID,"signin_login").click() # klik tombol sign in
        time.sleep(1)

        # validasi
        response_data = browser.find_element(By.ID,"swal2-title").text
        response_message = browser.find_element(By.ID,"swal2-content").text

        self.assertIn('not found', response_data)
        self.assertEqual(response_message, 'Email atau Password Anda Salah')

    def test_c_failed_login_with_special_password_character(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("http://barru.pythonanywhere.com/daftar") # buka situs
        time.sleep(3)
        browser.find_element(By.ID,"email").send_keys("agam@gmail.com") # isi email
        time.sleep(1)
        browser.find_element(By.ID,"password").send_keys("agam123@") # isi password
        time.sleep(1)
        browser.find_element(By.ID,"signin_login").click() # klik tombol sign in
        time.sleep(1)

        # validasi
        response_data = browser.find_element(By.ID,"swal2-title").text
        response_message = browser.find_element(By.ID,"swal2-content").text

        self.assertIn('Password tidak valid', response_data)
        self.assertEqual(response_message, 'Tidak boleh mengandung symbol')

    def test_d_failed_login_with_incorrect_email(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("http://barru.pythonanywhere.com/daftar") # buka situs
        time.sleep(3)
        browser.find_element(By.ID,"email").send_keys("agam@gmail") # isi email
        time.sleep(1)
        browser.find_element(By.ID,"password").send_keys("agam123") # isi password
        time.sleep(1)
        browser.find_element(By.ID,"signin_login").click() # klik tombol sign in
        time.sleep(1)

        # validasi
        response_data = browser.find_element(By.ID,"swal2-title").text
        response_message = browser.find_element(By.ID,"swal2-content").text

        self.assertIn('Email tidak valid', response_data)
        self.assertEqual(response_message, 'Cek kembali email anda')

    def test_e_failed_login_with_incorrect_password(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("http://barru.pythonanywhere.com/daftar") # buka situs
        time.sleep(3)
        browser.find_element(By.ID,"email").send_keys("agam@gmail.com") # isi email
        time.sleep(1)
        browser.find_element(By.ID,"password").send_keys("agam") # isi password
        time.sleep(1)
        browser.find_element(By.ID,"signin_login").click() # klik tombol sign in
        time.sleep(1)

        # validasi
        response_data = browser.find_element(By.ID,"swal2-title").text
        response_message = browser.find_element(By.ID,"swal2-content").text

        self.assertIn('not found', response_data)
        self.assertEqual(response_message, 'Email atau Password Anda Salah')

    def test_f_failed_login_with_empty_email(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("http://barru.pythonanywhere.com/daftar") # buka situs
        time.sleep(3)
        browser.find_element(By.ID,"email").send_keys("") # isi email
        time.sleep(1)
        browser.find_element(By.ID,"password").send_keys("agam123") # isi password
        time.sleep(1)
        browser.find_element(By.ID,"signin_login").click() # klik tombol sign in
        time.sleep(1)

        # validasi
        response_data = browser.find_element(By.ID,"swal2-title").text
        response_message = browser.find_element(By.ID,"swal2-content").text

        self.assertIn('Email tidak valid', response_data)
        self.assertEqual(response_message, 'Cek kembali email anda')

    def test_g_failed_login_with_empty_password(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("http://barru.pythonanywhere.com/daftar") # buka situs
        time.sleep(3)
        browser.find_element(By.ID,"email").send_keys("agam@gmail") # isi email
        time.sleep(1)
        browser.find_element(By.ID,"password").send_keys("") # isi password
        time.sleep(1)
        browser.find_element(By.ID,"signin_login").click() # klik tombol sign in
        time.sleep(1)

        # validasi
        response_data = browser.find_element(By.ID,"swal2-title").text
        response_message = browser.find_element(By.ID,"swal2-content").text

        self.assertIn('not found', response_data)
        self.assertEqual(response_message, 'Email atau Password Anda Salah')

    def tearDown(self): 
        self.browser.close()

if __name__ == "__main__": 
    unittest.main()