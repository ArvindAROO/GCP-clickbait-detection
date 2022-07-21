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
        
        title, text = getSummary(url) #get the relevant info from the article
        # KeywordsSimilarity, articlePercentSimilarity, nlpPercentSimilarity = findSimPercentage(title, keywords, articleSummary, nlpSummary) #find the similarity
        
        # finalSummaryPercentage = (articlePercentSimilarity + nlpPercentSimilarity) / 2 # average of two types
        
        final_wrapper_res = final_wrapper(title, text)
        final_res = final_wrapper_res["sim"]

        model_res = final_wrapper_res["model_sim"]

        category_res = final_wrapper_res["categories_sim"]

        similarityArray = [final_res, model_res, category_res]

        
        if all( similarityArray[i] < 50 for i in range(len(similarityArray))) or model_res < 9.99:
            verdict = "<br>The chances of this being a clickbait are high"
        else:
            verdict = "<br>The chances of this being a clickbait are low."
        similarityArray = [str(i)+ "%" for i in similarityArray]
        similarityArray[0] = "Final: " + similarityArray[0]
        similarityArray[1] = "Model Based: " + similarityArray[1]
        similarityArray[2] = "Category Based: " + similarityArray[2]

        return "<h3>Similarities-</h3>" + '<br>'.join(similarityArray) + verdict 
    except Exception as E:
        print(E)
        return "Summary not available for the current url"

if __name__ == "__main__":
    app.run(host='localhost', port=5000)