import trends_crawler
import pandas as pd

if __name__ == '__main__':
    url = 'https://getdaytrends.com/ko/korea/top/tweeted/day/'

    while True:
        print("What shall we do?\n1: crawl trends\n2: do colab")
        what_to_do = input()
        if what_to_do == "1":
            tweet = trends_crawler.twitter()
            trends_arr = tweet.trends(url)
            trends_arr = pd.DataFrame(trends_arr, columns=['hashtag'])
            trends_arr.to_csv('trends.tsv', index=False, sep="\t")
            print("csv file created!\ndone.\n")
        elif what_to_do == "2":
            tweet = trends_crawler.twitter()
            dataframe = pd.read_csv('trends.tsv')
            trends = []
            for i in range(len(dataframe) - 10):
                trends.append(dataframe.iloc[i, 0])
            tweet.init_work(trends)

        else:
            break
