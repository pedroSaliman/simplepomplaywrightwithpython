# models/search.py



class SearchPage:
    def __init__(self, page):
        
        self.page = page
        self.email = page.locator("#Email")
        self.password=page.locator("#Password")
        self.btn=page.locator("button[type='submit']")
        

    def navigate(self):
       

        self.page.goto("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")

    def search(self,theemail,thepass):
     self.email.is_visible()   
     self.email.fill("")
     self.email.fill(theemail)
     self.password.is_visible() 
     self.password.fill("")
     self.password.fill(thepass)
     self.btn.is_visible() 
     self.btn.click()
