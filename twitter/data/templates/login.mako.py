# -*- encoding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 7
_modified_time = 1328607511.879
_template_filename = 'd:\\twitter\\twitter\\templates/login.mako'
_template_uri = '/login.mako'
_source_encoding = 'ascii'
_exports = []


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'<html>\r\n  <head><meta http-equiv="content-type" content="text/html; charset=utf-8" />\r\n    <link rel="stylesheet" type="text/css" href="/static/twitter.css" />\r\n    <script type="text/javascript" src="/static/twitter.js"></script>\r\n  </head>\r\n  <body class="" onload="">\r\n    <div class="twitter-login-header">\r\n      <table width="100%" border="0" style="font-size:16px">\r\n        <tr>\r\n          <td align="left" width="90">\r\n            <h3>\r\n              <!-- @TODO (csharma): To move images to third_party folder. -->\r\n              <img alt="Twitter Gagdet" src="http://www.gstatic.com/ig/modules/twitter/twitterbird.cache.png"/>\r\n            </h3>\r\n          </td>\r\n          <td>\r\n            <div class="twitter-login">\r\n              <a href="http://twitter.com/" target="_blank" alt=""/>\r\n                <!-- @TODO (csharma): To move images to third_party folder. -->\r\n                <img src="http://www.gstatic.com/ig/modules/twitter/logo.cache.png" style="vertical-align:middle;border:0;"/>\r\n              </a>\r\n            </div>\r\n            <div id="login-button">\r\n              <a href="{{ login_url }}" target="loginPopUp" onclick="window.open(this.href,\'loginPopUp\',\'width=800,height=630,toolbar=0,location=0,directories=0,status=0,menubar=0,scrollbars=1,resizable=0\');return false;">\r\n                <img class="twitter-login" src="http://www.gstatic.com/ig/modules/twitter/sigin_btn.cache.png" alt="" style="border:0;padding-top:10px;"/>\r\n            </div>\r\n            <br/>\r\n          </td>\r\n        </tr>\r\n        <tr>\r\n          <td></td>\r\n          <td>\r\n            <div id="join-now">\r\n              Join the conversation <br/>\r\n              <a href="https://twitter.com/signup" target="_blank">\r\n                Sign up now\r\n              </a>\r\n            </div>\r\n          </td>\r\n        </tr>\r\n      </table>\r\n    </div>\r\n  </body>\r\n</html>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


