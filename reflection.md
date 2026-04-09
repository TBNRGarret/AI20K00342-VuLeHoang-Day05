Role cụ thể trong nhóm (không viết chung chung "thành viên")
Phần phụ trách cụ thể (liệt kê 2-3 đóng góp có output rõ)
SPEC phần nào mạnh nhất, phần nào yếu nhất? Vì sao?
Đóng góp cụ thể khác với mục 2 (ví dụ: test prompt, debug, support)
1 điều học được trong hackathon mà trước đó chưa biết
Nếu làm lại, đổi gì? (phải cụ thể, không viết "cố gắng hơn")
AI giúp gì? AI sai/mislead ở đâu? (bắt buộc nêu cả hai mặt)

# BÁO CÁO ĐÓNG GÓP CÁ NHÂN - HACKATHON

**Họ và tên:** Vũ Lê Hoàng
**Tên đội (Team):** XanhSM_D6

## 1. Vai trò trong dự án
**Chức danh cụ thể:** Kỹ sư Lõi AI (AI Core Engineer) 

## 2. Phần phụ trách cụ thể & Output
*(Dưới đây là các phần việc chính tôi đã đảm nhận)*

1. **[Xây dựng luồng Retrieval-Augmented Generation]**
   - **Chi tiết:** Cấu hình và thiết lập công cụ tìm kiếm kết nối cơ sở dữ liệu Vector với LLM.
   - **Output rõ ràng:** Hoàn thiện file `agent_graph.py` và `vector_tools.py`, bot có khả năng truy xuất chính xác top 5 tài liệu liên quan nhất với thời gian xử lý < 10s.

2. **[Tối ưu hóa System Prompt]**
   - **Chi tiết:** Thiết kế "nhân cách" và bộ quy tắc ứng xử cho AI dựa trên tài liệu của dự án.
   - **Output rõ ràng:** Một file `system_prompt_v4.py` hoàn chỉnh, giúp AI loại bỏ hoàn toàn tình trạng bịa đặt (hallucination) trong 50 test cases liên tiếp.

## 3. Đánh giá năng lực (SPEC)
   **Phần mạnh nhất:** [Xử lý Prompt]
   **Vì sao?** [Tôi có tư duy tốt trong việc chia nhỏ bài toán của user, dự đoán trước các kịch bản người dùng vặn vẹo AI để đặt rule rào trước trong prompt.]
   **Phần yếu nhất:** [Cấu hình môi trường & xử lý dependency (LangChain ecosystem)]
   **Vì sao?** [Tôi gặp khó khăn khi làm việc với các thư viện thay đổi nhanh như LangChain. Ví dụ, lỗi ModuleNotFoundError: langchain.tools.retriever xuất phát từ việc thư viện refactor nhưng tôi chưa nắm rõ structure mới (langchain_core, langchain_community).
   Việc này khiến tôi mất thời gian debug và thử nhiều cách (đổi import, downgrade version) trước khi hiểu đúng nguyên nhân. Điều này cho thấy tôi cần cải thiện kỹ năng đọc documentation chính thức và kiểm soát version.]

## 4. Các đóng góp cụ thể khác (Hỗ trợ & QA)
   **Kiểm thử (Test/QA):**
   Tôi đã tự viết script test retriever (test_retriever.py) để kiểm tra toàn bộ pipeline từ embedding → FAISS → SQLite. 
   **Gỡ lỗi (Debug):**
   Tôi trực tiếp debug các lỗi liên quan đến:
   Import sai module do LangChain đổi version
   Những lỗi này mang tính hệ thống, không chỉ là syntax, nên giúp tôi hiểu sâu hơn về pipeline.
   **Hỗ trợ team:**
   Tôi xây dựng một custom retriever dùng chung cho hệ thống, giúp team Data và team Agent có một interface thống nhất để truy xuất dữ liệu. Điều này giảm sự phụ thuộc giữa các thành viên và giúp việc tích hợp dễ dàng hơn.
## 5. Trải nghiệm học tập mới (Lessons Learned)

1 điều mới học được:
Tôi hiểu rõ cách xây dựng một pipeline RAG (Retrieval-Augmented Generation) hoàn chỉnh ở mức backend, bao gồm:

Vector hóa dữ liệu bằng embedding model (SentenceTransformers)
Lưu trữ và truy vấn bằng FAISS
Mapping dữ liệu gốc qua SQLite
Tích hợp retriever vào agent thông qua tool

Trước đây tôi chỉ sử dụng API AI ở mức đơn giản, nhưng qua bài này tôi hiểu rõ hơn cách hệ thống hoạt động phía sau, đặc biệt là cách dữ liệu được truy xuất và đưa vào context cho model.

## 6. Góc nhìn cải tiến (Retrospective)
Nếu làm lại, tôi sẽ thay đổi:
Tôi sẽ chuẩn hóa environment ngay từ đầu (fix version cụ thể cho LangChain, FAISS, embedding model) thay vì để đến khi lỗi mới xử lý.
Ngoài ra, tôi sẽ tạo một bộ dữ liệu nhỏ (mock data) để test retriever sớm, thay vì phụ thuộc hoàn toàn vào dữ liệu thật từ team Data. Điều này giúp phát hiện lỗi logic sớm hơn và giảm bottleneck khi tích hợp cuối.
## 7. Làm việc với AI (Đồng đội ảo)

AI đã làm RẤT TỐT ở việc:
AI hỗ trợ tôi rất tốt trong việc:

Gợi ý cấu trúc code cho retriever và FastAPI
Sinh các đoạn code xử lý embedding, FAISS search
Giải thích nhanh các lỗi phổ biến

Điều này giúp tôi tiết kiệm thời gian trong việc viết boilerplate và tập trung hơn vào logic chính.

AI đã SAI và GÂY HIỂU LẦM ở việc:
AI thường cung cấp code sử dụng API cũ của LangChain (deprecated), đặc biệt là các import path.
Ví dụ, AI gợi ý langchain.tools.retriever trong khi version hiện tại đã chuyển sang langchain_community. Điều này khiến tôi mất thời gian debug vì lỗi không nằm ở logic mà ở dependency.
Từ đó, tôi nhận ra rằng không thể phụ thuộc hoàn toàn vào AI, mà cần kiểm chứng lại bằng documentation chính thức hoặc source code.