# Google Drive Product Feedback Intelligence

This project builds an end to end product feedback intelligence system that takes raw Google Drive user feedback, analyzes it using a retrieval augmented generation pipeline, produces structured JSON for PM workflows, and can optionally send this structured output directly into Jira. The primary goal is to help product teams gain consistent insights, generate usable user stories, and standardize issue creation.

The system uses the following techniques:

* Retrieval Augmented Generation (RAG) for grounding model outputs in product documentation.
* A structured labeling pipeline to convert messy user feedback into a standardized JSON schema.
* A three part KPI framework to measure performance and reliability.
* A Gradio interface for non technical users.
* Optional Jira Cloud integration to automate issue creation.

---

## 1. Project Overview

Product feedback is often unstructured, inconsistent, and hard to compare. PM teams spend large amounts of time rewriting feedback, extracting labels, and creating Jira tickets. This project solves that by:

* Turning raw text feedback into structured JSON (sentiment, urgency, risk flag, product area, user story, and more).
* Using a RAG system to improve accuracy by retrieving relevant Drive documentation.
* Running KPIs to verify quality and explain differences between a baseline system and the RAG enhanced system.
* Offering a user friendly chatbot UI for manual evaluation and editing.
* Providing optional Jira automation for streamlined PM workflows.

The system outputs JSON that is ingestion ready for DataOps, dashboards, and product planning.

---

## 2. How to Run the System (Recommended: Google Colab)

The project is designed primarily for Google Colab.

### Step 1: Open the notebook in Colab

Upload the file:

```
Final_Project_BevoGPT.ipynb
```

Open it in Google Colab.

### Step 2: Upload required files to Colab

In the left sidebar of Colab, upload the following files:

#### a. Knowledge base text files

Place all text files used for retrieval into the Colab working directory:

```
Feature_Specifications.txt
Product_Architecture_Overview.txt
Known_Constraints.txt
UX_Rules_Behavior_Examples.txt
User_Personas.txt
Release_Notes.txt
Golden_User_Story_Examples.txt
Performance_Issues_Guide.txt
Feedback_labeling_guidelines.txt
```

#### b. Evaluation dataset

```
eval_dataset.json
```

All files must be uploaded separately. Colab treats them as individual files in the runtime environment.

### Step 3: Run the notebook top to bottom

Colab will prompt you at the correct steps:

* When the Azure API key is needed, Colab will ask for it interactively.
* Jira is disabled by default and will show a status message in the Gradio UI.

### Step 4: Launch the Gradio interface

At the end of the notebook, a Gradio link will appear.
Use this link to:

* Paste customer feedback
* Generate JSON output
* Edit the JSON if needed
* Optionally push it into Jira

---

## 3. Optional Local Execution (VS Code or Jupyter)

Although Colab is recommended, you can run the project locally.

### Step 1: Create a virtual environment

```
python -m venv venv
source venv/bin/activate        # macOS or Linux
venv\Scripts\activate           # Windows
```

### Step 2: Install dependencies

```
pip install -r requirements.txt
```

### Step 3: Place all `.txt` files and `eval_dataset.json` in the same folder as the notebook.

### Step 4: Open the `.ipynb` file in VS Code or Jupyter Notebook.

Gradio will launch in your browser.
Public share links work only from Colab.

---

## 4. Jira Integration (Optional)

### Jira is disabled by default

In the notebook, the Jira config is:

```python
JIRA_URL = ""
JIRA_EMAIL = ""
JIRA_API_TOKEN = ""
JIRA_PROJECT_KEY = "SCRUM"
```

Because URL, email, and token are blank, Jira stays disabled.
The Gradio UI will show a message indicating that Jira is unavailable, but all other features still work.

### How to enable Jira integration

1. Go to Atlassian
2. Open Jira
3. Create a Software Project
4. Choose a Scrum board
5. Find your project key (example: SCRUM)
6. In Atlassian Account Settings, create an API token
7. Copy your Jira Cloud URL (example: `https://yourdomain.atlassian.net`)
8. Paste values into the notebook fields:

```python
JIRA_URL = "https://yourdomain.atlassian.net"
JIRA_EMAIL = "your_email@example.com"
JIRA_API_TOKEN = "YOUR_API_TOKEN"
JIRA_PROJECT_KEY = "SCRUM"
```

### Sending issues to Jira

Once enabled:

* The Gradio UI displays green “Jira Enabled” status.
* The “Send to Jira” button converts the JSON into Atlassian Document Format and posts it using the Jira REST API.
* Jira will show new issues instantly on your Scrum board.

If Jira is disabled:

* The button returns a safe message:

  ```
  Jira is not configured. You can still copy this JSON manually.
  ```

---

## 5. KPIs and Evaluation Framework

The system is evaluated using three KPIs:

---

### **KPI 1: Faithfulness and Citation Rate**

This measures whether:

1. The summary stays faithful to the user’s text.
2. The product area is supported by retrieved documentation.

A grouped bar chart shows RAG vs baseline:

* RAG often improves citation correctness.
* Faithfulness is similar between both systems unless context is needed.

---

### **KPI 2: Useful Structure Rate**

This checks whether the JSON:

* Includes all required fields
* Uses valid label values
* Follows PM formatting rules
* Provides meaningful notes

A second bar chart compares pass rates:

* RAG produces more complete and actionable JSON.
* Baseline tends to miss notes and misclassify product areas.

---

### **KPI 3: User Story Alignment Score**

This compares:

* The generated user story
  versus
* The gold user story in `eval_dataset.json`

The score uses normalized similarity to capture how well phrasing, structure, and intention match.

RAG typically has higher alignment because of grounding in product context.

---

## 6. Gradio Interface

The Gradio UI offers a simple workflow:

1. Paste feedback into the left input box
2. Press “Analyze Feedback”
3. Receive structured JSON in the right panel
4. Edit JSON if needed
5. Optionally send to Jira

The same JSON is used for:

* Jira issue creation
* KPI benchmarking
* DataOps pipelines

The interface automatically detects Jira status and adjusts behavior.

---

## 7. Files Included in This Repository

Required:

* `Final_Project_BevoGPT.ipynb`
* `eval_dataset.json`
* `kb_files/` folder (or all `.txt` files individually)

Supporting:

* `README.md`
* `requirements.txt`

Not included:

* No API keys
* No Jira tokens
* No secrets of any kind

---

## 8. Security Note

The repository does not include:

* Azure API keys
* Jira API tokens
* .env files

All sensitive values are entered at runtime inside Colab.

---

## 9. Contact and Attribution

This project uses Azure OpenAI through UT’s gateway, LangChain for retrieval, FAISS for vector storage, and Gradio for the UI.

