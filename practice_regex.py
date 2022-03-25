import re
a = '''
해관(세관) 통계에 따르면 올해 1~2월 중국 휴대폰과 가전 제품 수출은 전년 같은 기간 대비 소폭 하락했다. 수줴팅(束珏婷) 상무부 대변인은 24일 상무부 정례 브리핑에서 언론이 제기한 홈코노미(Home+Economy) 상품의 수출 인기가 식고 있는 건 아닌가라는 질문에 다음과 같이 답변했다. 수 대변인은 "이에 대해 매우 중시하면서 면밀히 주시하고 있다"면서 "현재 중국의 대외무역 발전이 직면한 상황은 여전히 복잡하고 엄중하다"고 말했다. 수 대변인의 설명에 따르면 첫째, 코로나19 영향이 여전히 지속되고 있다. 세계 공급망 병목 현상이 아직 해소되지 않아 반도체 칩 등 중요한 원자재 부족이 대외무역 기업의 발목을 잡고 있다. 최근 전국 본토의 집단감염이 많은 곳에서 광범위하게 빈발하는 특징을 보이면서 대외무역 산업망과 공급망이 영향을 받았다. 둘째, 해외에서 방역 조치를 단계적으로 완화해 집에 머무는 시간이 감소하면서 일부 홈코노미 제품 수요가 상대적으로 감소했다. 셋째, 최근 지정학적 리스크가 상승하면서 벌크상품 가격이 치솟고 세계 경제∙무역 회복이 큰 불확실성에 직면하면서 해외 소비자들의 믿음이 타격을 입었다. 수 대변인은 "동시에 중국 무역 산업은 기반이 튼튼하고 산업망∙공급망의 회복력이 충분하다는 것을 봐야 한다"고 말했다. 이어 "올해 1~2월 중국의 무역액 규모는 전년 동기 대비 13.3% 증가한 6조 2000억 위안(약 1186조 9900억 원)을 기록, 안정적으로 출발했다"며 "당 중앙과 국무원의 강력한 리더십 아래 각 지역과 부처, 많은 대외무역 기업의 공동 노력 아래 연간 대외무역 운영을 합리적 구간에서 유지할 자신이 있다"고 덧붙였다.
'''
txt = re.split('\[가-힣.]+.', a)[0].split('\n')[1]
txt_freq = txt.split(' ')
freq = [txt.count(i) for i in txt_freq]
for i, j in enumerate(freq):
    if max(freq) == j:
        print(f'텍스트에서 가장 높은 빈도수인 {j}번 나타난 단어는 "{txt_freq[i]}"')
        
#결과: 텍스트에서 가장 높은 빈도수인 8번 나타난 단어는 "무역"

#뉴스기사 링크:http://kr.people.com.cn/n3/2022/0325/c414496-9976099.html
    
t = '''
The head of the International Monetary Fund (IMF) on Wednesday hailed the nomination of a South Korean IMF official, Rhee Chang-yong, to be the head of South Korea's central bank, calling him an outstanding leader and champion of analytical rigor. 
IMF Managing Director Kristalina Georgieva said Rhee will step down as director of the Asia and Pacific Department (APD) early next month to be considered for his new role as governor of the Bank of Korea.
"Since joining the Fund in February 2014, Chang-yong has been an outstanding institutional leader. 
He has brought a keen intellect and passion to his work, dedicating his efforts to serving our member countries," she said in a released statement. 
"During his eight years at the helm of APD, Chang-yong has made a tremendous impact in strengthening the Fund's relationship with Asian member countries. 
His vast knowledge of Asian economies and politics—as well as his wide network—have helped to forge trust with our members," she added, while asking others to join her in "congratulating Chang-yong on his nomination to this very important role."
Georgieva also said Rhee was a "steadfast colleague and a friend." 
"Those of us who had the privilege of working with him were deeply touched by his kindness and collegiality, as well as his marvelous sense of humor," she said. 
"He has been a people leader to the core, fully committed to the well-being of APD staff. 
He will be sorely missed by colleagues across the institution." 
The congratulatory remarks come amid a heated debate in South Korea over who should have nominated a new central bank governor with President Moon Jae-in set to step down in May.
Moon's office said the selection of Rhee had been made under discussions with, if not consent from, the aides of President-elect Yoon Suk-yeol, which was quickly refuted by Yoon's transition team.
Moon and Yoon were originally scheduled to meet after Yoon was elected president in the March 9 presidential election, but the meeting has yet to be held amid speculations the two sides were quarreling over who should name nominees to several key government posts that are expected to become vacant before Moon's term ends. 
Rhee previously worked as an economics professor at Seoul National University, vice chairman of the Financial Services Commission and chairman of the Securities and Futures Commission of Korea, according to the IMF.
He also served as chief economist at the Asian Development Bank until joining the IMF in 2014. (Yonhap)
'''
t = t.replace('\n', "")
t1 = re.split('\[(A-Za-z0-9).]', t)[0]
words = t1.split(' ')
abv_1 = [i for i in words if len(i) > 3]
freq = [t1.count(i) for i in abv_1]
most_freq = list(set([abv_1[i] for i, j in enumerate(freq) if max(freq) == j]))
#결과: ['said', 'Korea', 'with', 'over', 'Rhee']

for i, j in enumerate(freq):
    if max(freq) == j:
        print(f'텍스트에서 가장 높은 빈도수 {j}번 나타난 단어는 "{abv_1[i]}"')
        
'''결과: 텍스트에서 가장 높은 빈도수 5번 나타난 단어는 "Rhee"
텍스트에서 가장 높은 빈도수 5번 나타난 단어는 "said"
텍스트에서 가장 높은 빈도수 5번 나타난 단어는 "Rhee"
텍스트에서 가장 높은 빈도수 5번 나타난 단어는 "said"
텍스트에서 가장 높은 빈도수 5번 나타난 단어는 "with"
텍스트에서 가장 높은 빈도수 5번 나타난 단어는 "with"
텍스트에서 가장 높은 빈도수 5번 나타난 단어는 "said"
텍스트에서 가장 높은 빈도수 5번 나타난 단어는 "Rhee"
텍스트에서 가장 높은 빈도수 5번 나타난 단어는 "with"
텍스트에서 가장 높은 빈도수 5번 나타난 단어는 "Korea"
텍스트에서 가장 높은 빈도수 5번 나타난 단어는 "over"
텍스트에서 가장 높은 빈도수 5번 나타난 단어는 "with"
텍스트에서 가장 높은 빈도수 5번 나타난 단어는 "said"
텍스트에서 가장 높은 빈도수 5번 나타난 단어는 "Rhee"
텍스트에서 가장 높은 빈도수 5번 나타난 단어는 "over"
텍스트에서 가장 높은 빈도수 5번 나타난 단어는 "Rhee" '''
    
#뉴스기사 링크: http://news.koreaherald.com/view.php?ud=20220324000157&md=20220325003058_BL