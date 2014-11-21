from stdutils import prettyFunction, giveMenu, inputFraction, getFraction, prettyFraction

def calcPythag(leg, hyp):
    return getFraction(math.sqrt(hyp**2-leg**2))

def inputSin():
    opp = inputFraction("Opposite: ")
    hyp = inputFraction("Hypotinuse: ")
    adj = calcPythag(opp, hyp)

def printFunctions(opp, adj, hyp):
    opp = prettyFraction(opp, forceFloat=True)
    adj = prettyFraction(adj, forceFloat=True)
    hyp = prettyFraction(hyp, forceFloat=True)
    print("sin x = {}/{}".format(opp,hyp))
    print("cos x = {}/{}".format(adj,hyp))
    print("tan x = {}/{}".format(opp,adj))
    print("csc x = {}/{}".format(hyp,opp))
    print("sec x = {}/{}".format(hyp,adj))
    print("cot x = {}/{}".format(adj,opp))

