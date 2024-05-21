from .forms import CaptchaForm

def default_context(request):
    form = CaptchaForm(use_required_attribute=False)
    newsform = CaptchaForm(use_required_attribute=False, prefix='news')
    feedform = CaptchaForm(use_required_attribute=False, prefix='feed')
    return {'form': form, 'newsform': newsform, 'feedform': feedform}