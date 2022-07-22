# AI/ML tools in GCP

### Team Members:
- Anurag Khanra - PES1UG19CS090
- Arvind Krishna - PES1UG19CS090

### Setup
- ##### Requirements
	- GCP account with resources available
	- The auth token for the GCP user named as `key.json` in `API/`
	- Python3, pip & virtualenv

- ##### Usage
	- Clone the repository using `git clone git@github.com:ArvindAROO/GCP-clickbait-detection.git`
	- Create a virtualenv using `source venv/bin/activate # ./venv/Scripts/activate`
	- Activate the same with `virtualenv venv # python -m venv venv`
	- Install dependencies with `pip3 install -r requirements.txt`
	- Start the backend with `cd API && python app.py`
	- Load the `plugin/` folder into any Chromium-based browsers extension using _load unpacked_ option

### Working
- As soon as the button is clicked, the extension with a API call to the backend, with the link of the current website in included in the query
- The backend - A Flask app, fetches that websites by scraping the same, and seperates the _title_ & _body_ which will be used for further processing

### Usage of GCP
- #### Pretrained models
	- Using a pretrained [Cloud Natural Language API](https://cloud.google.com/natural-language) to find category of the text available in both the title & the body
	- Comparing them to each other could give a reasonable accuracy aboutwhether the body given is even related to the title
- #### AutoML Model
	- The [Dataset](), found on kaggle had 32000 rows with titles of news artciles which were classified as either `clickbait` or `not clickbait`
	- This dataset was cleaned and upload to _AutoML_ with _MultiLabel Classification_ and trained to a reasonable accuracy of _**???%**_ and deployed
	- Then our backend with fetch the title and send it to this endpoint, and get a response about it being a clickbait with its confidence
- The final result is the combonation of both of these at 60:40 ratio

### Example Images

