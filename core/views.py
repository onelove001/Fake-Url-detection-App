from django.shortcuts import *
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
import pickle


df = pd.read_csv("core/data.csv")

def index(request):
    context = {}
    return render(request, "index.html", context)


def home(request):
    context = {}
    return render(request, "home.html", context)


def data(request):

    context = {}
    return render(request, "data.html", context)


def accuracy(request):
    X = df.drop("CLASS_LABEL", axis=1)
    y = df["CLASS_LABEL"]
    X_train, X_test, y_train, y_test = train_test_split(X,y,test_size = 0.20, random_state=45)
    minmax = MinMaxScaler()
    minmax.fit(X_train)
    X_train = minmax.transform(X_train)
    X_test = minmax.transform(X_test)
    model = MultinomialNB()
    model.fit(X_train, y_train)
    predictionss = model.predict(X_test)
    acc = round(accuracy_score(y_test, predictionss) * 100, 1)
    print(confusion_matrix(y_test, predictionss))
    print(classification_report(y_test, predictionss))
    context = {"acc":acc}
    return render(request, "accuracy.html", context)


def prediction(request):
    import pickle
    check = None
    try:
        if request.method == "POST":
            id_no = request.POST.get("id_no")
            NumDots = request.POST.get("NumDots")
            SubdomainLevel = request.POST.get("SubdomainLevel")
            PathLevel = request.POST.get("PathLevel")
            UrlLength = request.POST.get("UrlLength")
            NumDash = request.POST.get("NumDash")
            NumDashInHostname = request.POST.get("NumDashInHostname")
            AtSymbol = request.POST.get("AtSymbol")
            TildeSymbol = request.POST.get("TildeSymbol")
            NumUnderscore = request.POST.get("NumUnderscore")
            NumPercent = request.POST.get("NumPercent")
            NumQueryComponents = request.POST.get("NumQueryComponents")
            NumAmpersand = request.POST.get("NumAmpersand")
            NumHash = request.POST.get("NumHash")
            NumNumericChars = request.POST.get("NumNumericChars")
            NoHttps = request.POST.get("NoHttps")
            RandomString = request.POST.get("RandomString")
            IpAddress = request.POST.get("IpAddress")
            DomainInSubdomains = request.POST.get("DomainInSubdomains")
            DomainInPaths = request.POST.get("DomainInPaths")
            HttpsInHostname = request.POST.get("HttpsInHostname")
            HostnameLength = request.POST.get("HostnameLength")
            PathLength = request.POST.get("PathLength")
            QueryLength = request.POST.get("QueryLength")
            DoubleSlashInPath = request.POST.get("DoubleSlashInPath")
            NumSensitiveWords = request.POST.get("NumSensitiveWords")
            EmbeddedBrandName = request.POST.get("EmbeddedBrandName")
            PctExtHyperlinks = request.POST.get("PctExtHyperlinks")
            PctExtResourceUrls = request.POST.get("PctExtResourceUrls")
            ExtFavicon = request.POST.get("ExtFavicon")
            InsecureForms = request.POST.get("InsecureForms")
            RelativeFormAction = request.POST.get("RelativeFormAction")
            ExtFormAction = request.POST.get("ExtFormAction")
            AbnormalFormAction = request.POST.get("AbnormalFormAction")
            PctNullSelfRedirectHyperlinks = request.POST.get("PctNullSelfRedirectHyperlinks")
            FrequentDomainNameMismatch = request.POST.get("FrequentDomainNameMismatch")
            FakeLinkInStatusBar = request.POST.get("FakeLinkInStatusBar")
            RightClickDisabled = request.POST.get("RightClickDisabled")
            PopUpWindow = request.POST.get("PopUpWindow")
            SubmitInfoToEmail = request.POST.get("SubmitInfoToEmail")
            IframeOrFrame = request.POST.get("IframeOrFrame")
            MissingTitle = request.POST.get("MissingTitle")
            ImagesOnlyInForm = request.POST.get("ImagesOnlyInForm")
            SubdomainLevelRT = request.POST.get("SubdomainLevelRT")
            UrlLengthRT = request.POST.get("UrlLengthRT")
            PctExtResourceUrlsRT = request.POST.get("PctExtResourceUrlsRT")
            AbnormalExtFormActionR = request.POST.get("AbnormalExtFormActionR")
            ExtMetaScriptLinkRT = request.POST.get("ExtMetaScriptLinkRT")
            PctExtNullSelfRedirectHyperlinksRT = request.POST.get("PctExtNullSelfRedirectHyperlinksRT")
            data = [[id_no,NumDots,SubdomainLevel,PathLevel,UrlLength,NumDash,NumDashInHostname,AtSymbol,TildeSymbol,NumUnderscore,NumPercent,NumQueryComponents,NumAmpersand,NumHash,NumNumericChars,NoHttps,RandomString,IpAddress,DomainInSubdomains,DomainInPaths,HttpsInHostname,HostnameLength,PathLength,QueryLength,DoubleSlashInPath,NumSensitiveWords,EmbeddedBrandName,PctExtHyperlinks,PctExtResourceUrls,ExtFavicon,InsecureForms,RelativeFormAction,ExtFormAction,AbnormalFormAction,PctNullSelfRedirectHyperlinks,FrequentDomainNameMismatch,FakeLinkInStatusBar,RightClickDisabled,PopUpWindow,SubmitInfoToEmail,IframeOrFrame,MissingTitle,ImagesOnlyInForm,SubdomainLevelRT,UrlLengthRT,PctExtResourceUrlsRT,AbnormalExtFormActionR,ExtMetaScriptLinkRT,PctExtNullSelfRedirectHyperlinksRT]]
            minmax = MinMaxScaler()
            minmax.fit(data)
            data = minmax.transform(data)
            with open('core/model' , 'rb') as f:
                model = pickle.load(f)
            prediction = model.predict(data)
            if data is not None:
                if prediction == 1:
                    check = True
                elif prediction == 0:
                    check = False
        
    except:
        pass
    context = {"check": check}
    return render(request, "prediction.html", context)