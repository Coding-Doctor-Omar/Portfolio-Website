# Instructions
To be able to run this web app locally for testing purposes, follow the steps below; otherwise, you can visit the website here: https://omars-devclinic.vercel.app/.

## Setting Up Environment Variables
### For Windows (CMD), run the following commands:
<pre>
setx APP_SECRET_KEY "any-secret-key-you-want"
</pre>

<pre>
setx sender_email "any-gmail-of-your-choice"
</pre>

Next, go to this article to learn how to generate a gmail app password: https://support.microsoft.com/en-us/office/gmail-two-factor-authentication-d37df22d-b300-442d-89d9-3892c342e38f.

After getting your gmail app password, run the following command:
<pre>
setx gmail_app_pass "your_gmail_app_password"
</pre>

If you had already started an IDE session, restart your session.

### For Linux or MacOS, follow the same steps as windows, but the 3 commands should be as follows:
##### macOS (Zsh):
<pre>
echo 'export APP_SECRET_KEY="any-secret-key-you-want"' >> ~/.zshrc
source ~/.zshrc
</pre>
<pre>
echo 'export sender_email="any-gmail-of-your-choice"' >> ~/.zshrc
source ~/.zshrc
</pre>
<pre>
echo 'export gmail_app_pass="your-gmail-app-password"' >> ~/.zshrc
source ~/.zshrc
</pre>

##### Linux or macOS (Bash):
<pre>
echo 'export APP_SECRET_KEY="any-secret-key-you-want"' >> ~/.bashrc
source ~/.bashrc
</pre>
<pre>
echo 'export sender_email="any-gmail-of-your-choice"' >> ~/.bashrc
source ~/.bashrc
</pre>
<pre>
echo 'export gmail_app_pass="your-gmail-app-password"' >> ~/.bashrc
source ~/.bashrc
</pre>

Note: If you're unsure whether you're using Bash or Zsh, you can run the following command in your terminal to find out: <pre>echo $SHELL</pre>



## Installing Dependencies from 'requirements.txt'

In your IDE session, run the following command in the terminal:
<pre>
pip install -r requirements.txt
</pre>


# Now, you should be able to run the web app locally from your IDE :)
