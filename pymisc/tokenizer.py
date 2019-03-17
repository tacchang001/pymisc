import re


class StringTokenizer:
    def __init__(self, text):  # トークンに分割
        self.tokens = re.split("[ \t\n\r\f,]", text)  # 正規表現で分割

    def next_token(self):
        # 次のトークンを得る（次のトークンに進む）
        token = self.tokens[0]
        self.tokens = self.tokens[1:]
        return token

    def has_more_tokens(self):
        # 次のトークンがあるかどうかを調べる
        return len(self.tokens) > 0


def main():
    import sys
    tl = ["get cur",
          "set cur TRY_JPY",
          "ger cur",
          "set cur",
          "set cur USD_JPY 120",
          "get prd",
          "set prd H4",
          "get prd",
          "get cnt",
          "set cnt 250",
          "get cnt"]
    for text in tl:
        try:
            print("text = {}".format(text))
            tokens = StringTokenizer(text)
            while tokens.has_more_tokens():
                t = tokens.next_token()
                sys.stdout.write("{}, ".format(t))
            print("")

        except Exception as er:
            print("ERROR : {}".format(er))


if __name__ == '__main__':
    main()
