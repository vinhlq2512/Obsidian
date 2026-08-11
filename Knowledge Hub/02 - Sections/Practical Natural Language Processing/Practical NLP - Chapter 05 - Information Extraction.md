---
type: reading-section
book: "[[Practical Natural Language Processing]]"
status: in_progress
chapter: 5
start_page: 293
end_page: 351
reading_date: 2026-08-07
planned_sessions:
  - "2026-08-07 | 293-310 | IE applications, tasks, pipeline, keyphrase, NER mở đầu | 55 phút"
  - "2026-08-08 | 311-330 | NER system, active learning, entity linking, RE mở đầu | 55 phút"
  - "2026-08-09 | 331-351 | Relationship extraction, event extraction, template filling | 55 phút"
tags:
  - nlp
  - practical-nlp
  - information-extraction
---

# Practical NLP - Chapter 05 - Information Extraction

## Mục tiêu cần hiểu

- Information extraction biến text tự do thành thực thể, quan hệ, sự kiện hoặc schema có cấu trúc.
- [[Named Entity Recognition]] chỉ là một phần của IE pipeline.
- Entity linking, relationship extraction và template filling mở rộng NER thành dữ liệu dùng được.

## Định nghĩa quan trọng

- [[Information Extraction]]
- [[Keyphrase Extraction]]
- [[Named Entity Recognition]]
- Named entity disambiguation
- [[Entity Linking]]
- [[Relation Extraction]]
- [[Event Extraction]]
- [[Template Filling]]
- [[Information Extraction Pipeline]]

## Mental model

```text
Text thô
-> mention / keyphrase
-> entity
-> entity linking
-> relation / event
-> structured record
```

## Phần cần biết

- Giá trị thực tế của IE nằm ở việc biến văn bản thành dữ liệu có thể query, đo lường, hoặc đưa vào workflow.
- Khi đọc, chú ý ranh giới giữa extraction, disambiguation và linking.
- [[Information Extraction Pipeline]] thường cần nhiều bước phân tích ngôn ngữ hơn text classification, nhưng không phải task IE nào cũng cần đủ mọi bước.

## IE Applications

### Vì sao IE cần thiết

```text
Unstructured text
-> extract entities / events / relations / fields
-> structured information
-> search / recommendation / chatbot / workflow
```

- [[Information Extraction]] là task trích thông tin liên quan từ text documents.
- Text là unstructured data: khác database/table có schema rõ, free-flowing text không cho biết sẵn thông tin nằm ở trường nào.
- Với thông tin có fixed pattern như address, phone number hoặc date, pattern-based extraction như regular expressions có thể tương đối đơn giản.
- Với thông tin như tên người, quan hệ giữa entities hoặc chi tiết calendar event, cần language processing sâu hơn.

### Tagging news and other content

- News và content mỗi ngày chứa nhiều entities/events đang xảy ra.
- Ngoài phân loại article bằng [[Text Classification]], search engines và recommendation systems còn cần tag các entities quan trọng trong text.
- Ví dụ Google News trích people, organizations, locations và events để reader đi trực tiếp tới news về entity cụ thể.
- Đây là IE ở dạng product: không chỉ biết article thuộc topic nào, mà còn biết article nói về ai/cái gì/sự kiện nào.

### Chatbots

- Chatbot cần hiểu question trước khi retrieve hoặc generate response.
- Ví dụ câu “What are the best cafes around the Eiffel Tower?” yêu cầu hệ thống nhận ra `Eiffel Tower` và `cafe`, rồi tìm cafes trong vùng liên quan tới Eiffel Tower.
- IE giúp tách các pieces of information cụ thể khỏi user query để downstream system dùng được.

### Social media

- Social media như Twitter chứa thông tin cập nhật nhanh và nhiều nhiễu.
- IE có thể trích informative excerpts phục vụ decision making, ví dụ traffic updates hoặc disaster relief efforts.
- Ứng dụng này nhấn mạnh yếu tố time-sensitive: thông tin không chỉ đúng, mà còn cần được trích nhanh từ dòng text liên tục.

### Forms and receipts

- Banking apps, bill scanning và receipt scanning thường kết hợp OCR với IE.
- OCR đọc chữ từ ảnh; IE trích các field có ý nghĩa như thông tin trên check, bill hoặc receipt.
- Sách không đi sâu hướng này trong chapter vì OCR là bước chính và không thuộc NLP processing pipeline của sách.

## IE Tasks

### Taxonomy task

```text
Text
-> keyphrase / keyword
-> named entity mention
-> entity disambiguation + linking
-> relation
-> event / temporal information
-> template slots
```

- IE là umbrella term cho nhiều task có độ phức tạp khác nhau. Mục tiêu chung là extract “knowledge” từ text.
- Với ví dụ bài báo New York Times về Apple, các task IE xuất hiện ở nhiều tầng:
- [[Keyphrase Extraction]] nhận ra bài nói về `buyback` hoặc `stock price`.
- [[Named Entity Recognition]] nhận diện `Apple` là organization và `Luca Maestri` là person.
- [[Entity Linking|Named entity disambiguation and linking]] phân biệt `Apple` là Apple Inc., không phải trái táo hay tổ chức khác.
- [[Relation Extraction]] trích quan hệ `Luca Maestri -> finance chief of -> Apple`.
- [[Event Extraction]] nhận ra bài nói về một event, ví dụ “Apple buys back stocks”, và link các bài khác nói về cùng event theo thời gian.
- Temporal information extraction trích time/date, hữu ích cho calendar apps và interactive personal assistants.
- [[Template Filling]] điền các slot trong template chuẩn từ dữ liệu đã extract, ví dụ weather report hoặc flight announcement.

### Độ khó và cách triển khai

- Các task IE cần mức NLP processing khác nhau.
- [[Keyphrase Extraction|KPE]] cần ít NLP processing nhất; một số thuật toán có thể dùng thêm POS tagging.
- [[Named Entity Recognition|NER]] là task được nghiên cứu nhiều và có nhiều giải pháp đã thử nghiệm.
- Các task như entity linking, relation extraction, event extraction và template filling thường khó hơn, cần preprocessing sâu hơn và model riêng cho task.
- Vì IE phụ thuộc domain mạnh, ví dụ finance, news, airlines, hệ thống IE trong industry thường là hybrid: rule-based + learning-based.
- Không phải task IE nào cũng “solved” đủ để có standard approach tốt cho production. Với task khó, sách nhắc việc dùng pay-as-you-use services từ các provider lớn như Microsoft, Google và IBM.
- Dataset cho IE thường chuyên biệt hơn text classification. Thay vì chỉ cần text -> category, IE cần annotation mịn hơn như span, entity identity, relation hoặc slot.
- IE thường đánh giá bằng precision, recall và F1 trên standard evaluation sets. Kết quả cũng phụ thuộc vào độ chính xác của các bước preprocessing trước đó.

## The General Pipeline for IE

![[practical-nlp-ie-pipeline-figure-5-3.png]]

**Ý chính:** Figure 5-3 cho thấy IE không phải một model đơn lẻ. Nó là chuỗi phân tích từ text thô tới các representation ngày càng giàu cấu trúc hơn.

Nguồn: [[Practical Natural Language Processing]] - Figure 5-3.

```text
Raw text
-> sentence segmentation
-> word tokenization
-> part-of-speech tagging
-> named entity recognition / syntactic parsing
-> coreference resolution / entity disambiguation
-> relation extraction / event extraction
```

- So với [[Text Classification]], IE cần fine-grained NLP processing hơn vì nhiều output nằm ở mức token/span/entity/relation thay vì label cấp document.
- Để nhận diện named entities như person hoặc organization, hệ thống có thể cần biết part-of-speech tags của words.
- Để liên kết nhiều reference về cùng một entity, ví dụ `Albert Einstein`, `Einstein`, `the scientist`, `he`, hệ thống cần coreference resolution.
- Các bước như POS tagging và coreference resolution không bắt buộc trong text classification, nhưng có thể rất quan trọng trong IE.
- Không phải mọi task IE đều cần toàn bộ pipeline. [[Keyphrase Extraction]] cần ít processing nhất; một số algorithm thêm POS tagging trước khi chọn keyphrases.
- Ngoài [[Named Entity Recognition]], các task IE còn lại thường cần preprocessing sâu hơn và model riêng cho từng task.
- Vì task IE phụ thuộc vào độ chính xác của preprocessing, khi tự thu thập data và train model IE cần tính cả lỗi lan truyền từ các bước trước.

## Keyphrase Extraction

![[practical-nlp-kpe-amazon-read-reviews-figure-5-4.png]]

**Ý chính:** Figure 5-4 minh họa KPE trong product: thay vì đọc toàn bộ review, người dùng chọn các phrase được nhắc nhiều để lọc nhanh nội dung liên quan.

Nguồn: [[Practical Natural Language Processing]] - Figure 5-4.

### KPE là gì

- [[Keyphrase Extraction|Keyword and phrase extraction]] là IE task trích các words/phrases quan trọng để nắm gist của document.
- KPE hữu ích cho search/information retrieval, automatic document tagging, recommendation systems và text summarization.
- KPE khác [[Named Entity Recognition]] ở mục tiêu: KPE tìm cụm ý chính của document, không nhất thiết tìm named entities.

### Hướng tiếp cận

- Hai hướng phổ biến là supervised learning và unsupervised learning.
- Supervised KPE cần corpora gồm text và keyphrases tương ứng; có thể dùng engineered features hoặc deep learning, nhưng tạo labeled dataset tốn thời gian và chi phí.
- Unsupervised KPE không cần labeled dataset, thường domain-agnostic hơn, nên phổ biến hơn trong ứng dụng thực tế.
- Sách ghi nhận research gần đây cho thấy state-of-the-art DL methods cho KPE không nhất thiết tốt hơn unsupervised approaches.

### Graph-based KPE

```text
Document
-> candidate words/phrases
-> weighted graph
-> score nodes by importance/connectivity
-> top-N keyphrases
```

- Các unsupervised KPE algorithm phổ biến biểu diễn words/phrases như nodes trong weighted graph.
- Weight biểu diễn mức quan trọng của keyphrase.
- Keyphrase được chọn dựa trên mức connected với phần còn lại của graph.
- Node quan trọng thường vừa đủ frequent vừa liên kết tốt với nhiều phần khác của text.
- Các graph-based approach khác nhau ở cách chọn candidate words/phrases và cách score graph.

### Implementing KPE

- Sách minh họa dùng `textacy` trên `spaCy` với hai thuật toán TextRank và SGRank.
- Recipe triển khai trong sách:

```text
Raw document
-> load text
-> create spaCy language pipeline
-> convert text into textacy/spaCy doc
-> run TextRank or SGRank
-> return top-N keyphrases with scores/weights
-> inspect and tune output
```

- TextRank và SGRank đều là graph-based keyword/keyphrase extraction algorithms, nhưng output có thể khác nhau đáng kể trên cùng một text.
- Ví dụ trong sách, TextRank trả nhiều cụm dài xoay quanh `natural language processing`, còn SGRank trả cả cụm như `statistical machine translation`, `research`, `late 1980`.
- Các quyết định triển khai cần chỉnh gồm độ dài n-gram, POS tags nên giữ/bỏ, preprocessing trước khi extract, và cách loại overlapping n-grams.
- Có thể thử nhiều implementation, ví dụ `textacy`, `gensim`, hoặc tự implement TextRank, rồi so sánh trước khi chọn.
- Với KPE, việc “implement” nên hiểu là tạo một loop thử nghiệm: chạy algorithm sẵn có, đọc output, chỉnh candidate selection/scoring/post-processing, rồi so sánh với nhu cầu của product.

### Practical advice

Practical advice của sách có thể hiểu như checklist debug KPE trong production:

```text
Raw text
-> choose useful text region
-> extract candidate n-grams
-> build graph + rank
-> remove overlap / bad patterns / extraction noise
-> add domain heuristics
-> final meaningful keyphrase list
```

- **Document length:** tạo candidate n-grams và graph nhạy với độ dài document. Một cách xử lý là không dùng toàn bộ text, mà dùng phần đầu M% và phần cuối N% vì introduction/conclusion thường chứa summary chính.
- **Overlapping keyphrases:** có thể xuất hiện các cụm chồng nhau như `buy back stock` và `buy back`. Vì mỗi keyphrase được rank độc lập, top-N có thể lặp ý. Có thể dùng similarity measure như cosine similarity giữa top-ranked keyphrases để giữ các cụm dissimilar hơn.
- **Unwanted patterns:** đôi khi keyphrase có pattern không mong muốn, ví dụ bắt đầu bằng preposition. Có thể chỉnh implementation hoặc encode rule/heuristic để loại pattern này.
- **Text extraction errors:** với PDF hoặc scanned images, lỗi extract text ảnh hưởng mạnh tới KPE vì KPE nhạy với sentence structure. Nên có post-processing để tạo final meaningful list ít noise.
- **Domain heuristics:** custom KPE thực tế có thể kết hợp graph-based algorithm sẵn có với list heuristic theo domain, ví dụ whitelist/blacklist pattern, phrase normalization hoặc rule loại phrase quá chung.
- Bài học chính: graph-based KPE là điểm bắt đầu tốt, nhưng production KPE cần vòng cleanup và tuning riêng cho dữ liệu thật.

## Named Entity Recognition

![[practical-nlp-ner-displacy-figure-5-6.png]]

**Ý chính:** Figure 5-6 minh họa NER bằng displaCy: text được tô các span và gán label như PERSON, ORG, DATE, GPE/NORP. Đây là output ở mức span/entity, không phải label cho toàn bộ document.

Nguồn: [[Practical Natural Language Processing]] - Figure 5-6.

### NER là gì

- [[Named Entity Recognition]] là IE task nhận diện entities trong document.
- Entities thường là person, location, organization, và các specialized strings như money expressions, dates, products, names/numbers of laws hoặc articles.
- KPE có thể bắt được tên entity nếu phrase đó quan trọng, nhưng KPE không được thiết kế riêng để tìm named entities. NER thì nhắm trực tiếp vào việc tìm entity mentions và entity types.

### Ví dụ search

- Query “Where was Albert Einstein born?” cần hệ thống nhận ra `Albert Einstein` là person trước khi tìm place of birth.
- Output như `Ulm, Germany` trong search result là ví dụ NER nằm trong một workflow lớn hơn: hiểu entity trong query, rồi dùng entity đó để tìm thuộc tính liên quan.

### Vai trò trong IE pipeline

- NER là một bước quan trọng trong nhiều NLP applications có [[Information Extraction]].
- NER thường là prerequisite cho các IE task sâu hơn như [[Relation Extraction]] và [[Event Extraction]], vì các task này cần biết entities nào đang xuất hiện trước khi trích relation/event.
- NER cũng hữu ích trong machine translation vì names không nhất thiết phải dịch khi dịch câu.
- Sách nhấn mạnh NER là một trong những task NLP thường gặp trong industry.

## Building an NER System

![[practical-nlp-ner-bio-training-data-figure-5-7.png]]

**Ý chính:** Figure 5-7 cho thấy dữ liệu train NER thường ở mức token với nhãn BIO. Đây là dấu hiệu rõ nhất rằng NER không phải document classification mà là sequence labeling.

Nguồn: [[Practical Natural Language Processing]] - Figure 5-7.

### Ba cách tiếp cận

```text
Known names only
-> Gazetteer lookup

Known linguistic patterns
-> Rule-based NER

Need generalization to unseen text
-> ML sequence labeling
```

- Cách đơn giản nhất là dùng [[Gazetteer]]: một collection lớn các person/organization/location names liên quan tới domain hoặc công ty của mình.
- Nếu phần lớn entities trong dữ liệu được phủ bởi gazetteer, đây là điểm khởi đầu tốt khi chưa có NER system sẵn.
- Nhưng gazetteer tạo ra các câu hỏi thực tế: làm sao xử lý tên mới, update database định kỳ, và theo dõi alias như `USA` với `United States`.
- Bước tiếp theo là rule-based NER: viết pattern dựa trên word tokens và POS tags.
- Ví dụ pattern `NNP was born` có thể gợi ý token mang POS `NNP` là person.
- Sách nhắc hai công cụ rule-based là Stanford NLP `RegexNER` và spaCy `EntityRuler`.

### ML-based NER và sequence labeling

- Hướng thực tế hơn là train ML model để dự đoán named entities trên unseen text.
- Với mỗi word, hệ thống phải quyết định có phải entity không, và nếu có thì là loại nào.
- Về mặt trực giác, nó giống classification ở Chapter 04, nhưng khác ở chỗ NER là [[Sequence Labeling]].
- Text classifier thường dự đoán label cho mỗi text độc lập với context xung quanh; còn sequence classifier dùng surrounding context để dự đoán current word.
- Ví dụ `Washington` không thể quyết định là person hay location nếu nhìn riêng lẻ; trong câu “Washington is a rainy state”, context mới cho thấy đây là location.
- Vì lý do đó, NER thường được model như sequence classification problem.
- Sách nhắc CRF là một training algorithm phổ biến cho sequence classifier trong NER.
- Notebook minh họa dùng dataset CONLL-03 và `sklearn-crfsuite` cùng các feature dựa trên word và POS tags.

### Dữ liệu train NER

- Để làm sequence classification, dữ liệu phải giữ được context ở mức sentence.
- Practical NLP dùng Figure 5-7 để minh họa format annotation trong CONLL-03.
- BIO notation:
  `B` = beginning of an entity
  `I` = inside an entity nhiều từ
  `O` = non-entity
- Ví dụ `Peter` là `B-PER`, `Such` là `I-PER` vì cùng thuộc một person name có hai từ.
- Entity một từ như `Essex`, `Yorkshire`, `Headingley` chỉ cần tag `B-ORG` hoặc `B-LOC`.

### Quy trình train

```text
Load dataset
-> Extract features
-> Train classifier
-> Evaluate on test set
```

- Sách nhấn mạnh các bước train NER ở mức cao vẫn giống pipeline text classifiers ở Chapter 04.
- Điểm khác biệt cốt lõi nằm ở loại dữ liệu, feature ngữ cảnh, và việc dùng sequence classifier thay vì classifier độc lập từng sample.

## Câu hỏi review

1. IE khác [[Text Classification]] ở câu hỏi đầu ra như thế nào?
2. Vì sao tagging news entity hữu ích cho search và recommendation?
3. Trong receipt/check scanning, OCR và IE đảm nhiệm hai vai trò khác nhau ra sao?
4. NER khác entity linking ở đâu?
5. Relationship extraction cần thêm thông tin gì so với nhận diện entity?
6. Template filling phù hợp với loại bài toán nào?
7. Các task IE trong ví dụ bài báo về Apple đi từ mức đơn giản tới phức tạp như thế nào?
8. Vì sao IE trong industry thường là hybrid system thay vì chỉ rule hoặc chỉ ML?
9. Vì sao dataset cho IE thường chuyên biệt hơn dataset text classification?
10. IE pipeline khác text classification pipeline ở điểm nào?
11. Vì sao coreference resolution hữu ích cho entity disambiguation, relation extraction hoặc event extraction?
12. Vì sao unsupervised KPE thường phổ biến hơn supervised KPE trong ứng dụng thực tế?
13. Graph-based KPE chọn keyphrase quan trọng dựa trên trực giác nào?
14. Khi đưa KPE vào production, những lỗi/caveat nào cần xử lý sau extraction?
15. Khi implement KPE bằng `textacy`, pipeline tối thiểu gồm những bước nào?
16. Vì sao cần so sánh TextRank, SGRank, `gensim` hoặc implementation tự viết trước khi chọn một cách?
17. Vì sao document length có thể làm KPE graph-based kém ổn định?
18. Vì sao top-N keyphrases vẫn cần de-duplication hoặc post-processing trước khi đưa vào product?
19. NER khác KPE ở mục tiêu output như thế nào?
20. Vì sao NER thường là prerequisite cho relation extraction và event extraction?
21. Trong ví dụ “Where was Albert Einstein born?”, NER giúp hệ thống làm bước gì trước khi tìm câu trả lời?
22. Khi nào gazetteer là điểm bắt đầu hợp lý cho NER, và giới hạn chính của nó là gì?
23. Rule-based NER đi xa hơn lookup table ở điểm nào?
24. Vì sao NER được xem là sequence labeling chứ không phải classification độc lập từng từ?
25. BIO notation mã hóa multi-word entity như thế nào?

## Gợi ý trả lời câu hỏi review

- Dùng ví dụ một hóa đơn, một tin tức hoặc một hồ sơ y tế để chỉ ra entity, relation và event.

## Liên kết

- [[Practical Natural Language Processing]]
- [[Information Extraction]]
- [[Text Classification]]
- [[Named Entity Recognition]]
- [[Keyphrase Extraction]]
- [[Entity Linking]]
- [[Relation Extraction]]
- [[Event Extraction]]
- [[Template Filling]]
- [[Information Extraction Pipeline]]
