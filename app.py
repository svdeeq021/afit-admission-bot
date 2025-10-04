# import streamlit as st
# from groq import Groq
# import os
# from pathlib import Path

# # ============================================================================
# # UNIVERSITY ADMISSION CHATBOT
# # ============================================================================
# # This bot answers questions about university admissions using RAG
# # (Retrieval Augmented Generation) with Groq's free API
# # ============================================================================

# st.set_page_config(
#     page_title="University Admission Assistant",
#     page_icon="",
#     layout="wide"
# )

# # ============================================================================
# # CONFIGURATION
# # ============================================================================

# # You'll add your Groq API key here (we'll get it for free in setup)
# GROQ_API_KEY = os.getenv("GROQ_API_KEY", "your-api-key-here")

# # Initialize Groq client
# if GROQ_API_KEY and GROQ_API_KEY != "your-api-key-here":
#     client = Groq(api_key=GROQ_API_KEY)
# else:
#     client = None

# # ============================================================================
# # KNOWLEDGE BASE - University Admission Information
# # ============================================================================
# # For now, we're using hardcoded FAQs. Later, we'll load from files.

# KNOWLEDGE_BASE = """
# AIR FORCE INSTITUTE OF TECHNOLOGY (AFIT) – ADMISSION INFORMATION

# ABOUT AFIT:
# The Air Force Institute of Technology (AFIT) is located in Kaduna, Nigeria, inside the Nigerian Air Force Base. 
# It is affiliated with the Nigerian Air Force but admits both civilians and military personnel. AFIT offers diploma, 
# undergraduate and postgraduate programmes in engineering, sciences, management, and technology.
# AFIT is accredited by the National Universities Commission (NUC) and recognized for its quality education in STEM fields.
# You can find more details here: https://afit.edu.ng/home/about-us/about-afit/

# Official Website: https://afit.edu.ng
# Location: Nigerian Air Force Base, Kaduna, Nigeria

# ------------------------------------------------------------
# ADMISSION REQUIREMENTS:

# O’Level:
# - Five (5) credits including English Language and Mathematics in not more than two sittings (WAEC, NECO, GCE).
# - Relevant science or business subjects required depending on chosen course.

# UTME (JAMB):
# - Candidates must choose AFIT as FIRST CHOICE.
# - Cut-off marks:
#   * Degree Programmes: 200 and above
#   * ND/Diploma Programmes: 180 and above
# - Correct UTME subject combination is mandatory. So check specific course requirements.

# Post-UTME Screening:
# - Compulsory for all applicants who meet the UTME/O’Level requirements.
# - Conducted via AFIT Portal.
# - Departmental cut-off marks may apply.

# Direct Entry (DE):
# - ND, NCE, IJMB, or equivalent with at least Upper Credit (some programmes accept Lower Credit).
# - Must also satisfy O’Level subject requirements.

# Special Requirements (Military Affiliation):
# - Candidates must be medically fit and may undergo a fitness assessment.
# - Background/security checks are routine.
# - Age limits are not rigidly published, but younger candidates (≤24 years for undergraduates) are often favored.

# ------------------------------------------------------------
# AVAILABLE PROGRAMMES:

# Undergraduate Degree Programmes (B.Sc / B.Eng):
# Engineering Courses:
# - Aerospace Engineering
# - Mechanical Engineering
# - Electrical/Electronics Engineering
# - Mechatronics Engineering
# - Telecommunication Engineering
# - Civil Engineering
# - Information and Communication Technology

# Compting  Courses:
# - Cyber Security
# - Computer Science

# Science Courses:
# - Physics with Electronics
# - Chemistry
# - Mathematics

# Social Science & Management Courses:
# - Statistics
# - Accounting
# - Business Administration
# - Marketing
# - Economics
# - International Relations

# ND/HND Programmes:
# - Aircraft Engineering Technology
# - Electrical/Electronics Engineering Technology
# - Business Administration and Management
# - Mechanical Engineering Technology
# - Explosive Ordnance Technology
# - Civil Engineering Technology

# Postgraduate Programmes:
# - PGD, M.Sc, and PhD in selected Engineering and Science disciplines 
#   (e.g. Aerospace, Electrical/Electronics, Mechanical, Materials Engineering, Computer Science).

# ------------------------------------------------------------
# FEES (2025/2026 SESSION):

# Tuition & Sundry Fees:
# - AEROSPACE ENGINEERING:
#     * 100 LEVEL & DEGREE: 136,300.00	
#     * 200 LEVEL: 99,800.00
#     * 300 LEVEL: 89,800.00
#     * 400 LEVEL: 94,800.00
#     * 500 LEVEL:  84,800.00
# - OTHER ENGINEERING:
#     * 100 LEVEL: 128,500.00	
#     * 200 LEVEL: 92,000.00
#     * 300 LEVEL: 82,000.00
#     * 400 LEVEL: 87,000.00
#     * 500 LEVEL: 77,000.00
# - FACULTY OF GROUND AND COMMUNICATION ENGINEERING:
#     * 100 LEVEL: 128,500.00	    
#     * 200 LEVEL: 92,000.00	   
#     * 300 LEVEL: 82,000.00	   
#     * 400 LEVEL: 87,000.00	        
#     * 500 LEVEL: 77,000.00
# - FACULTY OF SCIENCES:
#     * 100 LEVEL: 113,500.00	
#     * 200 LEVEL: 74,500.00	     
#     * 300 LEVEL: 84,500.00	    
#     * 400 LEVEL: 69,500.00
# - FACULTY OF COMPUTING:
#     * 100 LEVEL: 103,500.00	
#     * 200 LEVEL: 67,000.00	      
#     * 300 LEVEL: 77,000.00	           
#     * 400 LEVEL: 62,000.00 
# - FACULTY OF MANAGEMENT SCIENCES:
#     * 100 LEVEL: 98,500.00	
#     * 200 LEVEL: 67,000.00	   
#     * 300 LEVEL: 67,000.00	           
#     * 400 LEVEL: 62,000.00	 
# - ND/HND Programmes: 
# - NEW ND, PRE-HND & HND STUDENTS:
#     * AIRCRAFT ENGINEERING: 137,500.00	
#     * OTHER ENGINEERING: 122,500.00	
#     * NON-ENGINEERING: 112,500.00
# - RETURNING ND & HND STUDENTS:
#     * AIRCRAFT ENGINEERING: 82,000.00		
#     * OTHER ENGINEERING: 67,000.00	
#     * NON-ENGINEERING: 67,000.00
# *(Exact totals vary per programme; consult the AFIT schedule of fees.)*

# Other Payments:
# - Acceptance Fee: ₦20,000
# - Hostel/Accommodation: Afit provides limited hostel space on a first-come, first-served basis. They are a variety to choose from based on genders:
#     - Male Hostel (AVM Udeagulu) Block: ₦40,000
#     - Male Hostel Bungalow: ₦40,000
#     - 36 by One Hostel (Male): ₦150,000
#     - AFIT Block A and B (Female): ₦50,000
#     - 45 by One (Female) SB Abubakar Way: ₦100,000
#     - TETFUND (Female) 1 & 2: ₦150,000
#     - Princess Gimbiya (Male) Hostel SB Abubakar Way: ₦150,000
#     - NAFIL (Male): ₦75,000
#     - NAFIL I (Female): ₦75,000
#     - NAFIL II (Female): ₦150,000

# Source: https://afit.edu.ng/home/schedule-of-sundry-fees-for-2025-2026-academic-session/

# ------------------------------------------------------------
# APPLICATION PROCESS:

# 1. Register for JAMB UTME and choose AFIT as first choice.
# 2. Sit UTME and score the required cut-off.
# 3. Visit AFIT Admission Portal (https://portal.afit.edu.ng) and register for Post-UTME screening.
# 4. Upload O’Level, UTME results, and other required documents.
# 5. Attend screening (date announced on portal).
# 6. Check admission status via the AFIT portal.
# 7. If admitted, pay acceptance fee then complete registration and payment of school fees.

# ------------------------------------------------------------
# IMPORTANT DATES (2025/2026):

# - Application Opens: July 2025
# - Application Closes: September 2025
# - Screening Exercise: August–September 2025
# - Admission List Release: October/November 2025
# *(Always confirm on AFIT official website.)*

# ------------------------------------------------------------
# REQUIRED DOCUMENTS:

# - JAMB UTME result slip
# - O’Level result(s) (WAEC/NECO/GCE)
# - Birth Certificate or Declaration of Age
# - Local Government/State of Origin Certificate
# - Evidence of Post-UTME registration
# - Passport photographs
# - For DE applicants: ND/HND/IJMB transcripts or certificates

# ------------------------------------------------------------
# USEFUL LINKS:

# - Main Website: https://afit.edu.ng
# - Admission Portal: https://portal.afit.edu.ng
# - Check Admission Status: https://portal.afit.edu.ng/putme_result/
# - School Fees Payment: https://afit.edu.ng/home/schedule-of-sundry-fees-for-2025-2026-academic-session/
# - About AFIT: https://afit.edu.ng/home/about-us/about-afit/

# ------------------------------------------------------------
# CONTACT INFORMATION:

# - Admission Office Email: info@afit.edu.ng
# - Phone Numbers: +2349074411999, +2348155559571
# - Address: Nigerian Air Force Base, Kaduna, Nigeria

# ------------------------------------------------------------
# FREQUENTLY ASKED QUESTIONS:

# Q: Is AFIT a military institution?
# A: AFIT is affiliated with the Nigerian Air Force but admits both civilians and military personnel. It is not strictly a military school like NDA.

# Q: Can civilians apply?
# A: Yes, the majority of AFIT students are civilians.

# Q: What is the cut-off mark for AFIT?
# A: 200 and above for degree programmes; 160 and above for ND/diploma programmes.

# Q: Does AFIT accept second choice candidates?
# A: No. AFIT must be chosen as first choice.

# Q: What is the dress code?
# A: Civilian students dress normally (corporate or decent casuals). There’s no military uniform requirement.

# Q: Does AFIT provide accommodation?
# A: Yes, but hostel spaces are limited and allocated on a first-come, first-served basis.

# Q: Does AFIT accept IJMB for admission?
# A: Yes, candidates with IJMB can apply through Direct Entry.

# Q: Are there age restrictions?
# A: Officially not published, but younger candidates are preferred (16–24 years for undergraduates).

# Q: Is AFIT accredited by NUC?
# A: Yes, AFIT’s degree programmes are NUC-accredited.

# Q: Can students proceed to postgraduate studies at AFIT?
# A: Yes, AFIT offers PGD, Masters, and PhD programmes in selected disciplines.

# ------------------------------------------------------------
# """


# # ============================================================================
# # HELPER FUNCTIONS
# # ============================================================================

# def search_knowledge_base(query):
#     """
#     Simple keyword search in knowledge base.
#     In production, we'd use vector embeddings for better search.
#     """
#     query_lower = query.lower()
#     relevant_sections = []
    
#     # Simple keyword matching
#     keywords = {
#         'requirement': 'ADMISSION REQUIREMENTS',
#         'program': 'AVAILABLE PROGRAMS',
#         'course': 'AVAILABLE PROGRAMS',
#         'apply': 'APPLICATION PROCESS',
#         'fee': 'TUITION FEES',
#         'cost': 'TUITION FEES',
#         'date': 'IMPORTANT DATES',
#         'when': 'IMPORTANT DATES',
#         'contact': 'CONTACT INFORMATION'
#     }
    
#     for keyword, section in keywords.items():
#         if keyword in query_lower:
#             # Extract the relevant section
#             start = KNOWLEDGE_BASE.find(section)
#             if start != -1:
#                 end = KNOWLEDGE_BASE.find('\n\n', start + len(section))
#                 if end == -1:
#                     end = len(KNOWLEDGE_BASE)
#                 relevant_sections.append(KNOWLEDGE_BASE[start:end])
    
#     # If no specific keywords matched, return general info
#     if not relevant_sections:
#         return KNOWLEDGE_BASE[:500]  # Return first 500 chars
    
#     return '\n\n'.join(relevant_sections)


# def get_ai_response(user_question, context):
#     """
#     Get response from Groq AI with context from knowledge base
#     """
#     if not client:
#         return "⚠️ Please set up your Groq API key to use the chatbot. Check the sidebar for instructions!"
    
#     try:
#         # Create prompt with context
#         prompt = f"""You are a helpful university admission assistant. Answer the student's question using ONLY the information provided in the context below. If the answer is not in the context, say you don't have that specific information and suggest contacting the admission office.

# CONTEXT:
# {context}

# STUDENT QUESTION: {user_question}

# ANSWER (be friendly, concise, and helpful):"""

#         # Call Groq API
#         response = client.chat.completions.create(
#             model="llama-3.1-8b-instant",  # Fast and free model
#             messages=[
#                 {"role": "system", "content": "You are a helpful university admission assistant."},
#                 {"role": "user", "content": prompt}
#             ],
#             temperature=0.7,
#             max_tokens=500
#         )
        
#         return response.choices[0].message.content
        
#     except Exception as e:
#         return f"❌ Error: {str(e)}\n\nPlease check your API key or internet connection."


# # ============================================================================
# # STREAMLIT UI
# # ============================================================================

# # Sidebar - Setup Instructions
# st.sidebar.image("afit.png", use_container_width=True)
# with st.sidebar:
#     st.title("🎓 Setup Guide")
#     st.markdown("""
#     ### Quick Setup:
    
#     1. **Get Free Groq API Key**
#        - Go to: [console.groq.com](https://console.groq.com)
#        - Sign up (free)
#        - Create API key
    
#     2. **Add API Key**
#        - Copy your key
#        - Paste in input below
       
#     3. **Start Chatting!**
#     """)
    
#     # API Key input
#     api_key_input = st.text_input(
#         "Groq API Key",
#         type="password",
#         value=GROQ_API_KEY if GROQ_API_KEY != "your-api-key-here" else "",
#         help="Get your free key at console.groq.com"
#     )
    
#     if api_key_input and api_key_input != GROQ_API_KEY:
#         GROQ_API_KEY = api_key_input
#         client = Groq(api_key=GROQ_API_KEY)
#         st.success("✅ API Key updated!")
    
#     st.divider()
#     st.markdown("### About")
#     st.info("This chatbot helps students applying for admission into the Air Force Institute if Technology answer questions using AI.")

# # Main content
# st.image("afitlogo.png", width=1000)
# import streamlit as st

# 

# # Initialize chat history in session state
# if "messages" not in st.session_state:
#     st.session_state.messages = []
#     # Add welcome message
#     st.session_state.messages.append({
#         "role": "assistant",
#         "content": "Hello! 👋 I'm your University Admission Assistant. I can help you with:\n\n- Admission requirements\n- Available programs\n- Application process\n- Tuition fees\n- Important dates\n- Contact information\n- And any other information regarding AFIT\n\nWhat would you like to know?"
#     })

# # Display chat history
# for message in st.session_state.messages:
#     with st.chat_message(message["role"]):
#         st.markdown(message["content"])

# # Chat input
# if prompt := st.chat_input("Type your question here..."):
#     # Add user message to chat
#     st.session_state.messages.append({"role": "user", "content": prompt})
#     with st.chat_message("user"):
#         st.markdown(prompt)
    
#     # Get AI response
#     with st.chat_message("assistant"):
#         with st.spinner("Thinking..."):
#             # Search knowledge base for relevant context
#             context = search_knowledge_base(prompt)
            
#             # Get AI response
#             response = get_ai_response(prompt, context)
            
#             st.markdown(response)
    
#     # Add assistant response to chat
#     st.session_state.messages.append({"role": "assistant", "content": response})

# # Footer
# st.divider()
# st.markdown("""
# <div style='text-align: center; color: gray; font-size: 0.8em;'>
# Built by Svdeeq21 using Streamlit and Groq AI | 
# <a href='https://github.com/yourusername/university-admission-bot'>View on GitHub</a>
# </div>
# """, unsafe_allow_html=True)
import streamlit as st
from groq import Groq
import os
from pathlib import Path

# ============================================================================
# UNIVERSITY ADMISSION CHATBOT
# ============================================================================
# This bot answers questions about university admissions using RAG
# (Retrieval Augmented Generation) with Groq's free API
# ============================================================================

st.set_page_config(
    page_title="AFIT Admission Assistant",
    page_icon="afit.png",
    layout="wide"
)

# ============================================================================
# CONFIGURATION
# ============================================================================

# You'll add your Groq API key here (we'll get it for free in setup)
GROQ_API_KEY = os.getenv("GROQ_API_KEY", "your-api-key-here")

# Initialize Groq client
if GROQ_API_KEY and GROQ_API_KEY != "your-api-key-here":
    client = Groq(api_key=GROQ_API_KEY)
else:
    client = None

# ============================================================================
# KNOWLEDGE BASE - University Admission Information
# ============================================================================
# For now, we're using hardcoded FAQs. Later, we'll load from files.

KNOWLEDGE_BASE = """
# AIR FORCE INSTITUTE OF TECHNOLOGY (AFIT) – ADMISSION INFORMATION

# ABOUT AFIT:
# The Air Force Institute of Technology (AFIT) is located in Kaduna, Nigeria, inside the Nigerian Air Force Base. 
# It is affiliated with the Nigerian Air Force but admits both civilians and military personnel. AFIT offers diploma, 
# undergraduate and postgraduate programmes in engineering, sciences, management, and technology.
# AFIT is accredited by the National Universities Commission (NUC) and recognized for its quality education in STEM fields.
# You can find more details here: https://afit.edu.ng/home/about-us/about-afit/

# Official Website: https://afit.edu.ng
# Location: Nigerian Air Force Base, Kaduna, Nigeria

# ------------------------------------------------------------
# ADMISSION REQUIREMENTS:

# O’Level:
# - Five (5) credits including English Language and Mathematics in not more than two sittings (WAEC, NECO, GCE).
# - Relevant science or business subjects required depending on chosen course.

# UTME (JAMB):
# - Candidates must choose AFIT as FIRST CHOICE.
# - Cut-off marks:
#   * Degree Programmes: 200 and above
#   * ND/Diploma Programmes: 180 and above
# - Correct UTME subject combination is mandatory. So check specific course requirements.

# Post-UTME Screening:
# - Compulsory for all applicants who meet the UTME/O’Level requirements.
# - Conducted via AFIT Portal.
# - Departmental cut-off marks may apply.

# Direct Entry (DE):
# - ND, NCE, IJMB, or equivalent with at least Upper Credit (some programmes accept Lower Credit).
# - Must also satisfy O’Level subject requirements.

# Special Requirements (Military Affiliation):
# - Candidates must be medically fit and may undergo a fitness assessment.
# - Background/security checks are routine.
# - Age limits are not rigidly published, but younger candidates (≤24 years for undergraduates) are often favored.

# ------------------------------------------------------------
# AVAILABLE PROGRAMMES:

# Undergraduate Degree Programmes (B.Sc / B.Eng):
# Engineering Courses:
# - Aerospace Engineering
# - Mechanical Engineering
# - Electrical/Electronics Engineering
# - Mechatronics Engineering
# - Telecommunication Engineering
# - Civil Engineering
# - Information and Communication Technology

# Compting  Courses:
# - Cyber Security
# - Computer Science

# Science Courses:
# - Physics 
# - Physics with Electronics
# - Chemistry
# - Mathematics

# Social Science & Management Courses:
# - Statistics
# - Accounting
# - Business Administration
# - Marketing
# - Economics
# - International Relations

# ND/HND Programmes:
# - Aircraft Engineering Technology
# - Electrical/Electronics Engineering Technology
# - Business Administration and Management
# - Mechanical Engineering Technology
# - Explosive Ordnance Technology
# - Civil Engineering Technology

# Postgraduate Programmes:
# - PGD, M.Sc, and PhD in selected Engineering and Science disciplines 
#   (e.g. Aerospace, Electrical/Electronics, Mechanical, Materials Engineering, Computer Science).

# ------------------------------------------------------------
# FEES (2025/2026 SESSION):

# Tuition & Sundry Fees:
# - AEROSPACE ENGINEERING:
#     * 100 LEVEL & DEGREE: 136,300.00	
#     * 200 LEVEL: 99,800.00
#     * 300 LEVEL: 89,800.00
#     * 400 LEVEL: 94,800.00
#     * 500 LEVEL:  84,800.00
# - OTHER ENGINEERING:
#     * 100 LEVEL: 128,500.00	
#     * 200 LEVEL: 92,000.00
#     * 300 LEVEL: 82,000.00
#     * 400 LEVEL: 87,000.00
#     * 500 LEVEL: 77,000.00
# - FACULTY OF GROUND AND COMMUNICATION ENGINEERING:
#     * 100 LEVEL: 128,500.00	    
#     * 200 LEVEL: 92,000.00	   
#     * 300 LEVEL: 82,000.00	   
#     * 400 LEVEL: 87,000.00	        
#     * 500 LEVEL: 77,000.00
# - FACULTY OF SCIENCES:
#     * 100 LEVEL: 113,500.00	
#     * 200 LEVEL: 74,500.00	     
#     * 300 LEVEL: 84,500.00	    
#     * 400 LEVEL: 69,500.00
# - FACULTY OF COMPUTING:
#     * 100 LEVEL: 103,500.00	
#     * 200 LEVEL: 67,000.00	      
#     * 300 LEVEL: 77,000.00	           
#     * 400 LEVEL: 62,000.00 
# - FACULTY OF MANAGEMENT SCIENCES:
#     * 100 LEVEL: 98,500.00	
#     * 200 LEVEL: 67,000.00	   
#     * 300 LEVEL: 67,000.00	           
#     * 400 LEVEL: 62,000.00	 
# - ND/HND Programmes: 
# - NEW ND, PRE-HND & HND STUDENTS:
#     * AIRCRAFT ENGINEERING: 137,500.00	
#     * OTHER ENGINEERING: 122,500.00	
#     * NON-ENGINEERING: 112,500.00
# - RETURNING ND & HND STUDENTS:
#     * AIRCRAFT ENGINEERING: 82,000.00		
#     * OTHER ENGINEERING: 67,000.00	
#     * NON-ENGINEERING: 67,000.00
# *(Exact totals vary per programme; consult the AFIT schedule of fees.)*

# Other Payments:
# - Acceptance Fee: ₦20,000
# - Hostel/Accommodation: Afit provides limited hostel space on a first-come, first-served basis. They are a variety to choose from based on genders:
#     - Male Hostel (AVM Udeagulu) Block: ₦40,000
#     - Male Hostel Bungalow: ₦40,000
#     - 36 by One Hostel (Male): ₦150,000
#     - AFIT Block A and B (Female): ₦50,000
#     - 45 by One (Female) SB Abubakar Way: ₦100,000
#     - TETFUND (Female) 1 & 2: ₦150,000
#     - Princess Gimbiya (Male) Hostel SB Abubakar Way: ₦150,000
#     - NAFIL (Male): ₦75,000
#     - NAFIL I (Female): ₦75,000
#     - NAFIL II (Female): ₦150,000

# Source: https://afit.edu.ng/home/schedule-of-sundry-fees-for-2025-2026-academic-session/

# ------------------------------------------------------------
# APPLICATION PROCESS:

# 1. Register for JAMB UTME and choose AFIT as first choice.
# 2. Sit UTME and score the required cut-off.
# 3. Visit AFIT Admission Portal (https://portal.afit.edu.ng) and register for Post-UTME screening.
# 4. Upload O’Level, UTME results, and other required documents.
# 5. Attend screening (date announced on portal).
# 6. Check admission status via the AFIT portal.
# 7. If admitted, pay acceptance fee then complete registration and payment of school fees.

# ------------------------------------------------------------
# IMPORTANT DATES (2025/2026):

# - Application Opens: July 2025
# - Application Closes: September 2025
# - Screening Exercise: August–September 2025
# - Admission List Release: October/November 2025
# *(Always confirm on AFIT official website.)*

# ------------------------------------------------------------
# REQUIRED DOCUMENTS:

# - JAMB UTME result slip
# - O’Level result(s) (WAEC/NECO/GCE)
# - Birth Certificate or Declaration of Age
# - Local Government/State of Origin Certificate
# - Evidence of Post-UTME registration
# - Passport photographs
# - For DE applicants: ND/HND/IJMB transcripts or certificates

# ------------------------------------------------------------
# USEFUL LINKS:

# - Main Website: https://afit.edu.ng
# - Admission Portal: https://portal.afit.edu.ng
# - Check Admission Status: https://portal.afit.edu.ng/putme_result/
# - School Fees Payment: https://afit.edu.ng/home/schedule-of-sundry-fees-for-2025-2026-academic-session/
# - About AFIT: https://afit.edu.ng/home/about-us/about-afit/

# ------------------------------------------------------------
# CONTACT INFORMATION:

# - Admission Office Email: info@afit.edu.ng
# - Phone Numbers: +2349074411999, +2348155559571
# - Address: Nigerian Air Force Base, Kaduna, Nigeria

# ------------------------------------------------------------
# FREQUENTLY ASKED QUESTIONS:

# Q: Is AFIT a military institution?
# A: AFIT is affiliated with the Nigerian Air Force but admits both civilians and military personnel. It is not strictly a military school like NDA.

# Q: Can civilians apply?
# A: Yes, the majority of AFIT students are civilians.

# Q: What is the cut-off mark for AFIT?
# A: 200 and above for degree programmes; 160 and above for ND/diploma programmes.

# Q: Does AFIT accept second choice candidates?
# A: No. AFIT must be chosen as first choice.

# Q: What is the dress code?
# A: Civilian students dress normally (corporate or decent casuals). There’s no military uniform requirement.

# Q: Does AFIT provide accommodation?
# A: Yes, but hostel spaces are limited and allocated on a first-come, first-served basis.

# Q: Does AFIT accept IJMB for admission?
# A: Yes, candidates with IJMB can apply through Direct Entry.

# Q: Are there age restrictions?
# A: Officially not published, but younger candidates are preferred (16–24 years for undergraduates).

# Q: Is AFIT accredited by NUC?
# A: Yes, AFIT’s degree programmes are NUC-accredited.

# Q: Can students proceed to postgraduate studies at AFIT?
# A: Yes, AFIT offers PGD, Masters, and PhD programmes in selected disciplines.

# ------------------------------------------------------------
# """
# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def search_knowledge_base(query):
    """
    Enhanced keyword search that finds relevant sections in knowledge base.
    """
    query_lower = query.lower()
    relevant_sections = []
    
    # Expanded keyword mapping with more variations
    keywords = {
        # Admission related
        'requirement': ['ADMISSION REQUIREMENTS', 'REQUIRED DOCUMENTS'],
        'entry': ['ADMISSION REQUIREMENTS'],
        'olevel': ['ADMISSION REQUIREMENTS'],
        'jamb': ['ADMISSION REQUIREMENTS'],
        'utme': ['ADMISSION REQUIREMENTS'],
        'cutoff': ['ADMISSION REQUIREMENTS'],
        'cut-off': ['ADMISSION REQUIREMENTS'],
        'screening': ['ADMISSION REQUIREMENTS', 'APPLICATION PROCESS'],
        'postutme': ['ADMISSION REQUIREMENTS', 'APPLICATION PROCESS'],
        'direct entry': ['ADMISSION REQUIREMENTS'],
        
        # Programs/Courses
        'program': ['AVAILABLE PROGRAMMES'],
        'course': ['AVAILABLE PROGRAMMES'],
        'degree': ['AVAILABLE PROGRAMMES'],
        'engineering': ['AVAILABLE PROGRAMMES'],
        'aerospace': ['AVAILABLE PROGRAMMES'],
        'computer': ['AVAILABLE PROGRAMMES'],
        'science': ['AVAILABLE PROGRAMMES'],
        'management': ['AVAILABLE PROGRAMMES'],
        'hnd': ['AVAILABLE PROGRAMMES'],
        
        # Fees
        'fee': ['FEES'],
        'cost': ['FEES'],
        'tuition': ['FEES'],
        'price': ['FEES'],
        'payment': ['FEES'],
        'acceptance': ['FEES', 'APPLICATION PROCESS'],
        'hostel': ['FEES'],
        'accommodation': ['FEES'],
        
        # Application
        'apply': ['APPLICATION PROCESS'],
        'application': ['APPLICATION PROCESS'],
        'register': ['APPLICATION PROCESS'],
        'portal': ['APPLICATION PROCESS', 'USEFUL LINKS'],
        
        # Dates
        'date': ['IMPORTANT DATES'],
        'when': ['IMPORTANT DATES'],
        'deadline': ['IMPORTANT DATES'],
        'timeline': ['IMPORTANT DATES'],
        
        # Contact
        'contact': ['CONTACT INFORMATION'],
        'phone': ['CONTACT INFORMATION'],
        'email': ['CONTACT INFORMATION'],
        'address': ['CONTACT INFORMATION'],
        
        # General
        'about': ['ABOUT AFIT'],
        'location': ['ABOUT AFIT', 'CONTACT INFORMATION'],
        'military': ['ABOUT AFIT', 'FREQUENTLY ASKED QUESTIONS'],
        'civilian': ['FREQUENTLY ASKED QUESTIONS'],
        'faq': ['FREQUENTLY ASKED QUESTIONS'],
    }
    
    # Find matching sections
    matched_sections = set()
    for keyword, sections in keywords.items():
        if keyword in query_lower:
            for section in sections:
                matched_sections.add(section)
    
    # Extract the relevant sections from knowledge base
    for section_name in matched_sections:
        start = KNOWLEDGE_BASE.find(section_name)
        if start != -1:
            # Find the end (look for the separator line or next section)
            end = KNOWLEDGE_BASE.find('------------------------------------------------------------', start + 10)
            if end == -1:
                end = len(KNOWLEDGE_BASE)
            relevant_sections.append(KNOWLEDGE_BASE[start:end])
    
    # If no specific match, try to find FAQ answer
    if not relevant_sections:
        faq_start = KNOWLEDGE_BASE.find('FREQUENTLY ASKED QUESTIONS')
        if faq_start != -1:
            # Return FAQ section
            relevant_sections.append(KNOWLEDGE_BASE[faq_start:])
    
    # If still nothing, return general info
    if not relevant_sections:
        return KNOWLEDGE_BASE[:800]  # Return more context
    
    return '\n\n'.join(relevant_sections)


def get_ai_response(user_question, context):
    """
    Get response from Groq AI with context from knowledge base
    """
    if not client:
        return "⚠️ Please set up your Groq API key to use the chatbot. Check the sidebar for instructions!"
    
    try:
        # Create prompt with context
        prompt = f"""You are a helpful AFIT (Air Force Institute of Technology) admission assistant. Your job is to help prospective students with admission-related questions.

IMPORTANT INSTRUCTIONS:
- Use ONLY the information from the CONTEXT below
- Be specific with numbers, dates, and requirements when they are provided
- If the context has the answer, provide it clearly and completely
- If information is not in the context, politely say you don't have that specific information and direct them to contact the admission office
- Be friendly and professional
- Break down complex information into clear points

CONTEXT:
{context}

STUDENT QUESTION: {user_question}

ANSWER:"""

        # Call Groq API
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",  # Fast and free model
            messages=[
                {"role": "system", "content": "You are a helpful university admission assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=500
        )
        
        return response.choices[0].message.content
        
    except Exception as e:
        return f"❌ Error: {str(e)}\n\nPlease check your API key or internet connection."


# ============================================================================
# STREAMLIT UI
# ============================================================================

# Sidebar - Setup Instructions
with st.sidebar:
    st.title("🎓 Setup Guide")
    st.markdown("""
    ### Quick Setup:
    
    1. **Get Free Groq API Key**
       - Go to: [console.groq.com](https://console.groq.com)
       - Sign up (free)
       - Create API key
    
    2. **Add API Key**
       - Copy your key
       - Paste in input below
       
    3. **Start Chatting!**
    """)
    
    # API Key input
    api_key_input = st.text_input(
        "Groq API Key",
        type="password",
        value=GROQ_API_KEY if GROQ_API_KEY != "your-api-key-here" else "",
        help="Get your free key at console.groq.com"
    )
    
    if api_key_input and api_key_input != GROQ_API_KEY:
        GROQ_API_KEY = api_key_input
        client = Groq(api_key=GROQ_API_KEY)
        st.success("✅ API Key updated!")
    
    st.divider()
    st.markdown("### About")
    st.info("This AI chatbot helps prospective students with AFIT admission questions using official information from afit.edu.ng")

# Main content
# ------------------------------------------------------------------------------
# The one i started using
# st.image("afitlogo.png", width=1000)
# Then this one
# st.markdown(
#     """
#     <div style="text-align: center;">
#         <img src="your_image.png" width="300">
#     </div>
#     """,
#     unsafe_allow_html=True
# )

# Later settled with this layout
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image("afitlogo.png", use_container_width=True)
st.markdown("<h1 style='text-align: center;'>🎓 AFIT Admission Assistant</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Ask me anything about Air Force Institute of Technology admissions, requirements, programs, fees, or deadlines!</p>", unsafe_allow_html=True)
# Initialize chat history in session state
if "messages" not in st.session_state:
    st.session_state.messages = []
    # Add welcome message
    st.session_state.messages.append({
        "role": "assistant",
        "content": """Hello! 👋 Welcome to the **AFIT Admission Assistant**!

I can help you with information about:
- 📋 Admission requirements (O'Level, JAMB, Post-UTME)
- 📚 Available programmes (Engineering, Computing, Sciences, Management)
- 💰 Tuition fees and accommodation costs
- 📅 Important dates and deadlines
- 📝 Application process
- 🏢 Contact information
- ❓ Frequently asked questions

What would you like to know about AFIT?"""
    })

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Type your question here..."):
    # Add user message to chat
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Get AI response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            # Search knowledge base for relevant context
            context = search_knowledge_base(prompt)
            
            # Get AI response
            response = get_ai_response(prompt, context)
            
            st.markdown(response)
    
    # Add assistant response to chat
    st.session_state.messages.append({"role": "assistant", "content": response})

# Footer
st.divider()
st.markdown("""
<div style='text-align: center; color: gray; font-size: 0.8em;'>
Built for AFIT Admissions by Sadiq Shehu Musa | Powered by AI | 
<a href='https://github.com/svdeeq021/afit-admission-bot'>View on GitHub</a>
</div>
""", unsafe_allow_html=True)