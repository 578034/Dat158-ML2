import pickle

class CustomFormatter:
    def __init__(self,form):
        self.device_browser         = form.device_browser.data
        self.device_operatingSystem = form.device_operatingSystem.data
        self.device_isMobile        = form.device_isMobile.data
        self.geoNetwork_continent   = form.geoNetwork_continent.data
        self.geoNetwork_country     = form.geoNetwork_country.data.lower().capitalize()
        self.df = self.fillFrame()
        self.string = "\n\tBrowser: " + self.device_browser + "\n\tOS: " + self.device_operatingSystem + "\n\tIs mobile: " + self.device_isMobile + "\n\tContinent: " + self.geoNetwork_continent + "\n\tCountry: " + self.geoNetwork_country
        