import pandas as pd

import trends_crawler

if __name__ == "__main__":
    url = "https://getdaytrends.com/ko/korea/top/tweeted/day/"
    total_trend = 0
    while True:
        print("What shall we do?\n1: crawl trends\n2: do colab\n3: merge all results")
        what_to_do = input()
        if what_to_do == "1":
            tweet = trends_crawler.twitter()
            trends_arr = tweet.trends(url)
            trends_arr = pd.DataFrame(trends_arr, columns=["hashtag"])
            trends_arr.to_csv("trends.tsv", index=False, sep="\t")
            print("csv file created!\ndone.\n")
        elif what_to_do == "2":
            tweet = trends_crawler.twitter()
            dataframe = pd.read_csv("trends.tsv")
            trends = []
            total_trend = len(dataframe) - 10
            for i in range(total_trend):
                trends.append(dataframe.iloc[i, 0])
            tweet.init_work(trends)
        elif what_to_do == "3":
            ds = pd.read_csv("0.tsv", delimiter="\t")
            for i in range(total_trend):
                ds1 = pd.read_csv(str(i) + ".tsv", delimiter="\t")
                ds = pd.concat([ds, ds1], ignore_index=True)
            ds.to_csv("result.tsv", index=False, sep="\t")
        else:
            break
