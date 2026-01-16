# 🌍 AI Travel Planner for Students

Planning trips can be time-consuming and expensive, especially for students on a limited budget.  
This project uses **Generative AI (Google Gemini)** to create **personalized, budget-friendly travel itineraries** based on destination, duration, budget, and travel style.

---

## ✨ Features

- 🎓 Student-focused travel planning
- 💰 Budget-friendly itineraries
- 🗓️ Day-wise travel plans
- 🍽️ Affordable food recommendations
- 🚕 Cheap local transport options
- 🏨 Budget accommodation tips
- 💡 Student travel hacks
- ⚡ Powered by Google Gemini AI

---

## 🛠️ Tech Stack

- **Python**
- **Streamlit** (Frontend)
- **Google Gemini API** (Generative AI)
- **python-dotenv** (Environment variables)

---

## 📂 Project Structure

```

ai-travel-planner/
│── app.py
│── requirements.txt
│── .env
│── README.md

````

---

## 🚀 Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/ai-travel-planner.git
cd ai-travel-planner
````

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv .venv
```

Activate the environment:

**Windows**

```bash
source .venv/Scripts/activate
```

**Linux / macOS**

```bash
source .venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Set Gemini API Key

Create a `.env` file in the root directory:

```env
GEMINI_API_KEY=your_gemini_api_key_here
```

Or export directly (temporary):

**Windows (PowerShell)**

```powershell
setx GEMINI_API_KEY "YOUR_API_KEY"
```

**Linux / macOS**

```bash
export GEMINI_API_KEY="YOUR_API_KEY"
```

> ⚠️ **Never commit your API key to GitHub**

---

### 5️⃣ Run the Application

```bash
streamlit run app.py
```

The app will open automatically in your browser.

---

## 🧠 How It Works

1. User enters:

   * Destination
   * Number of days
   * Budget
   * Travel style
2. The app sends a structured prompt to **Gemini AI**
3. Gemini generates a **custom travel itinerary**
4. Results are displayed instantly in the Streamlit UI

---

## 📸 Screenshots

*(Add screenshots of the UI here for better presentation)*

---

## 🔮 Future Enhancements

* 🗺️ Google Maps integration
* 📊 Cost breakdown charts
* 📄 Export itinerary as PDF
* 🌦️ Weather-based suggestions
* 🏨 Real-time hotel & transport prices

---

## 🎯 Use Cases

* College students
* Budget travelers
* Hackathons & academic projects
* AI + Web development learning

---

## 📜 License

This project is licensed under the **MIT License**.

---

## 🤝 Contributing

Contributions are welcome!
Feel free to fork the repository and submit a pull request.

---

## ⭐ Acknowledgements

* Google Gemini API
* Streamlit Community

---

**Built with ❤️ for students who love to travel smart.**
