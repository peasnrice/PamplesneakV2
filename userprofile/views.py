from django.shortcuts import render_to_response, RequestContext
from django.contrib.auth.decorators import login_required

@login_required
def user_profile(request):
    user = request.user
    profile = user.profile
    args = {}
    return render_to_response('userprofile/profile.html', args, context_instance=RequestContext(request))