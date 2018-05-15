def alphabet_war(r, a):
    for num,x in enumerate(list(a)):
        if num < len(x):
            if x[num] == '*':
                x.replace(x[num], 'bang')
                print(x)



reinforces=[
    "g964xxxxxxxx",
    "myjinxin2015",
    "steffenvogel",
    "smile67xxxxx",
    "giacomosorbi",
    "freywarxxxxx",
    "bkaesxxxxxxx",
    "vadimbxxxxxx",
    "zozofouchtra",
    "colbydauphxx" 
]
airstrikes=[
    "* *** ** ***",
    " ** * * * **",
    " * *** * ***",
    " **  * * ** ",
    "* ** *   ***",
    "***   ",
    "**",
    "*",
    "*" 
]
alphabet_war(reinforces, airstrikes)