# 抓取内容的正则
dic_info_re= {
    'li_begin':'<div class="job-primary">',
    'job_url':'<a href="([\s\S]*?)"',
    'job_title':'<div class="job-title">([\s\S]*?)</div>',
    'job_salary':'<span class="red">([\s\S]*?)</span>',
    'job_keypoint':'<div class="tags"><span>([\s\S]*?)</div>',
    'job_place': '</h3>[\s\S]*?<p>([\s\S]*?)<em class="vline">',
    'job_exp': '</em>([\s\S]*?)<em',
    'job_edu':'</em>([\s\S]*?)</p>',
    'cmp_name':'<div class="info-company">[\s\S]*?<div class="company-text">[\s\S]*?<h3 class="name"><a href="[\s\S]*?>([\s\S]*?)</a></h3>',
    'cmp_emps':'<p>[\s\S]*?(\d+[\s\S]*?)</p>',
    'li_end':'</div>.*?</div>.*?</li>'
}
boss_info_list=['job_url','job_title','job_salary','job_keypoint','job_place', 'job_exp', 'job_edu','cmp_name', 'cmp_emps','job_type','job_desc','cmp_detail']
boss_create_sql="""
CREATE TABLE boss_info
       (ID INT PRIMARY KEY     NOT NULL,
       job_type             CHAR(100),
       job_title            TEXT,
       job_url              CHAR(100),
       job_salary           CHAR(100),
       job_keypoint         CHAR(100),
       job_place            CHAR(100),  
       job_exp              CHAR(100),
       job_edu              CHAR(100),
       cmp_name             CHAR(100),
       cmp_emps             CHAR(100),
       job_desc             TEXT,
       cmp_detail             TEXT)
"""
boss_head={
    'authority':'www.zhipin.com',
'method':'GET',
'path':'/job_detail/?query=python&page=1',
'scheme':'https',
'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
'accept-encoding':'gzip, deflate, br',
'accept-language':'zh-CN,zh;q=0.9',
'referer':'https//www.zhipin.com/job_detail/?query=python%E7%88%AC%E8%99%AB',
'upgrade-insecure-requests':'1',
'cookie': 'lastCity=101280600; JSESSIONID=""; __c=1523782004; __g=-; __l=l=%2Fwww.zhipin.com%2Fjob_detail%2F%3Fquery%3Dpython%26page%3D1&r=; __a=12790871.1523580316.1523580329.1523782004.5.3.1.5; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1523580318,1523782009; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1523782009',
'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}


dic_detail_re={
    'job_desc':'<div class="job-sec">.*?<h3>职位描述</h3>.*? <div class="text">(.*?)</div>.*?</div>',
    'cmp_detail':'<h3>公司介绍</h3>.*?<div class="text">(.*?)</div>'
}

'''
<div class="job-primary">[\s\S]*?<a href="([\s\S]*?)"[\s\S]*?<div class="job-title">([\s\S]*?)</div>[\s\S]*?<span class="red">([\s\S]*?)</span>[\s\S]*?<div class="tags"><span>([\s\S]*?)</div>[\s\S]*?</h3>[\s\S]*?<p>([\s\S]*?)</p>[\s\S]*?</em>([\s\S]*?)<em[\s\S]*?</em>([\s\S]*?)</p>[\s\S]*?<div class="info-company">[\s\S]*?<div class="company-text">[\s\S]*?<h3 class="name"><a href="[\s\S]*?>([\s\S]*?)</a></h3>[\s\S]*?<p>[\s\S]*?(\d+[\s\S]*?)</p>[\s\S]*?
<div class="job-primary">.*?<a href="([\s\S]*?)".*?<div class="job-title">([\s\S]*?)</div>.*?<span class="red">([\s\S]*?)</span>.*?<div class="tags"><span>([\s\S]*?)</div>.*?</h3>[\s\S]*?<p>([\s\S]*?)</p>.*?</em>([\s\S]*?)<em.*?</em>([\s\S]*?)</p>.*?<div class="info-company">[\s\S]*?<div class="company-text">[\s\S]*?<h3 class="name"><a href="[\s\S]*?>([\s\S]*?)</a></h3>.*?<p>[\s\S]*?(\d+[\s\S]*?)</p>.*?

'''
