# **InstaChecker 🕵🏻**

Identify Instagram accounts you follow that don't follow you back using the Instagram data export feature for analysis.

## **Features**
- Extracts followers and following data from Instagram's `.html` files.
- Outputs a clean list of accounts you follow but who don't follow you back.
- Easy to use and privacy-focused (all data remains on your local machine).


## **How It Works**
1. Download your Instagram data export from the platform.
2. Provide the `followers.html` and `following.html` files to this script.
3. Get a list of accounts that are not following you back.


## **Installation**
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/InstaChecker.git
   cd InstaChecker
   ```

2. **Install Dependencies**:
   Ensure you have Python 3 installed. Then, install the required library:
   ```bash
   pip install beautifulsoup4
   ```

## **How to Obtain Your Instagram Data**
1. Log in to Instagram on a browser or the app.
2. Go to **Settings** > **Privacy and Security**.
3. Under **Data Download**, click **Request Download**.
4. Choose the format as **HTML** and submit your request.
5. Instagram will send a link to download your data within 48 hours.
6. Extract the `.zip` file and locate (in the `followers_and_following` folder):
   - `followers.html`
   - `following.html`

## **Usage Instructions**
1. Place `followers.html` and `following.html` in the same directory as the script.
2. Run the script:
   ```bash
   python instachecker.py
   ```
3. View the output in your terminal, which lists the accounts you follow but who don’t follow you back.

## **Contributing**
Feel free to submit issues or pull requests if you encounter any bugs or have suggestions for improvement.

## **License**
This project is licensed under the MIT License.