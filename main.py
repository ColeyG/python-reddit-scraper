import prawRequest

prawRequest.PrawRequest().req("art", 1000, ["images"])
prawRequest.PrawRequest().req("pics", 1000, ["images"])
prawRequest.PrawRequest().req("pic", 1000, ["images"])
prawRequest.PrawRequest().req("pictures", 1000, ["images"])
prawRequest.PrawRequest().req("images", 1000, ["images"])
# schedule.every(1).minutes.do(prawRequest.PrawRequest().req("dog", 1))
