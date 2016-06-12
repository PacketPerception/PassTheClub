from django import forms


class SiteswapValidator(forms.Form):
    siteswap = forms.CharField()
