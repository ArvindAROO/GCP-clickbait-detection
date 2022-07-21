# flask app
from flask import Flask, request
from newsScraper import getSummary

# from percentage import findSimPercentage

from get_sim import final_wrapper

app = Flask(__name__)

@app.route("/url", methods=['GET'])
def main():
    try:
        url = request.args.get('query') #the url to be checked
        # print(url)
        
        title, text = getSummary(url) #get the relevant info from the article
        # KeywordsSimilarity, articlePercentSimilarity, nlpPercentSimilarity = findSimPercentage(title, keywords, articleSummary, nlpSummary) #find the similarity
        
        # finalSummaryPercentage = (articlePercentSimilarity + nlpPercentSimilarity) / 2 # average of two types
        
        # print(title)
        

        final_wrapper_res = final_wrapper(title, text)
        final_res = final_wrapper_res["sim"]

        model_res = final_wrapper_res["model_sim"]

        title_category = final_wrapper_res["categories"]["title"]

        body_category = final_wrapper_res["categories"]["body"]

        category_res = final_wrapper_res["categories_sim"]

        # print('title_category + body_category')
        # print(title_category)
        # print(body_category)

        similarityArray = [final_res * 100, model_res * 100, category_res * 100]
        print(similarityArray)
        
        if all( similarityArray[i] < 50 for i in range(len(similarityArray))) or similarityArray[1] < 9.99:
            verdict = "<br>The chances of this being a clickbait are high"
        else:
            verdict = "<br>The chances of this being a clickbait are low."
        similarityArray = [str(round(i, 3))+ "%" for i in similarityArray]
        similarityArray[0] = "Final: " + similarityArray[0]
        similarityArray[1] = "Model Based: " + similarityArray[1]
        similarityArray[2] = "Category Based: " + similarityArray[2]

        return "<h3>Categories</h3><b>Title</b> - " + ', '.join(title_category) + "<br><b>Body</b> - " + ', '.join(body_category) + "<h3>Similarities-</h3>" + '<br>'.join(similarityArray) + verdict 
    except Exception as E:
        print(E)
        return "Summary not available for the current URL"

if __name__ == "__main__":
    app.run(host='localhost', port=5000, debug=True)