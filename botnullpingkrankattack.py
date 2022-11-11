import requests

def sendRequest():
    r = requests.post("https://fastcomments.com/comments/vvQIdSqRq/U8w-AsUoPdv/vote?urlId=397553&broadcastId=4008d399-3742-497c-b471-5519e20e2973", headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}, data={"voteDir":"up","commentId":"U8w-AsUoPdv","urlId":"397553","url":"https://igg-games.com/herranwalt-lawyers-legacy-free-download.html"}) 
    if 'success' in r.text:
        print("Success new like!")
    else:
        print("Very big error" + str(r.status_code))
while True:
    sendRequest()