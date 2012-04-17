<html>
  <head><meta http-equiv="content-type" content="text/html; charset=utf-8" />
    <link rel="stylesheet" type="text/css" href="/static/twitter.css" />
    <script type="text/javascript" src="/static/twitter.js"></script>
  </head>
  <body class="" onload="">
    <div class="twitter-login-header">
      <table width="100%" border="0" style="font-size:16px">
        <tr>
          <td align="left" width="90">
            <h3>
              <!-- @TODO (csharma): To move images to third_party folder. -->
              <img alt="Twitter Gagdet" src="http://www.gstatic.com/ig/modules/twitter/twitterbird.cache.png"/>
            </h3>
          </td>
          <td>
            <div class="twitter-login">
              <a href="http://twitter.com/" target="_blank" alt=""/>
                <!-- @TODO (csharma): To move images to third_party folder. -->
                <img src="http://www.gstatic.com/ig/modules/twitter/logo.cache.png" style="vertical-align:middle;border:0;"/>
              </a>
            </div>
            <div id="login-button">
              <a href="{{ login_url }}" target="loginPopUp" onclick="window.open(this.href,'loginPopUp','width=800,height=630,toolbar=0,location=0,directories=0,status=0,menubar=0,scrollbars=1,resizable=0');return false;">
                <img class="twitter-login" src="http://www.gstatic.com/ig/modules/twitter/sigin_btn.cache.png" alt="" style="border:0;padding-top:10px;"/>
            </div>
            <br/>
          </td>
        </tr>
        <tr>
          <td></td>
          <td>
            <div id="join-now">
              Join the conversation <br/>
              <a href="https://twitter.com/signup" target="_blank">
                Sign up now
              </a>
            </div>
          </td>
        </tr>
      </table>
    </div>
  </body>
</html>
