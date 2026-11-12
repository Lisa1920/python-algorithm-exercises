class BrowserHistory:
    def __init__(self, start_url=None):
        self.back_stack = []
        self.forward_stack = []
        self.current_url = start_url

    def visit(self, new_url):
        if new_url == self.current_url:
            return self.current_url

        if self.current_url is not None:
            self.back_stack.append(self.current_url)

        self.current_url = new_url
        self.forward_stack.clear()
        return self.current_url

    def back(self):
        if self.back_stack:
            self.forward_stack.append(self.current_url)
            self.current_url = self.back_stack.pop()
        return self.current_url

    def forward(self):
        if self.forward_stack:
            self.back_stack.append(self.current_url)
            self.current_url = self.forward_stack.pop()
        return self.current_url


if __name__ == "__main__":
    browser = BrowserHistory("https://shop.example/home")
    browser.visit("https://shop.example/products")
    browser.visit("https://shop.example/product/42")

    print("Current page:", browser.current_url)
    print("Back:", browser.back())
    print("Forward:", browser.forward())

    browser.visit("https://shop.example/product/42")
    print("After opening the current page again:", browser.current_url)
    print("Back history:", browser.back_stack)
