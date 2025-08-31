# GENAI Psychologist 🧠💬

An AI-powered mental health support application that provides compassionate, intelligent conversations to help users with their mental wellness journey. Built with modern web technologies and advanced AI capabilities.

## 🌟 Features

- **Intelligent Chat Interface**: Engage in meaningful conversations with an AI psychologist
- **Responsive Design**: Seamless experience across desktop and mobile devices
- **Privacy-Focused**: Secure and confidential mental health support
- **User-Friendly Interface**: Clean, accessible design for easy navigation
- **Resource Center**: Access to mental health resources and information
- **Contact & About Pages**: Learn more about the platform and get in touch

## 🛠️ Tech Stack

### Frontend (Next.js)
- **Framework**: Next.js 14+ with App Router
- **Language**: TypeScript
- **Styling**: Tailwind CSS
- **UI Components**: Custom components with shadcn/ui
- **Icons**: Lucide React icons

### Backend (FastAPI)
- **Framework**: FastAPI
- **Language**: Python 3.8+
- **AI Integration**: Advanced language models for therapeutic conversations
- **Configuration**: Environment-based settings

## 📁 Project Structure

```
GENAI-psychologist/
├── aimentalhealth/          # Frontend (Next.js)
│   ├── app/
│   │   ├── components/      # Reusable React components
│   │   ├── chat/           # Chat interface page
│   │   ├── about/          # About page
│   │   ├── contact/        # Contact page
│   │   ├── resources/      # Resources page
│   │   └── ...
│   ├── components/ui/       # UI component library
│   └── ...
└── backend/                 # Backend (FastAPI)
    ├── app.py              # Main application file
    ├── config.py           # Configuration settings
    ├── tools.py            # Utility functions
    ├── requirements.txt    # Python dependencies
    └── ...
```

## 🚀 Getting Started

### Prerequisites

- Node.js 18+ and npm/yarn
- Python 3.8+
- Git

### Installation & Setup

#### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/GENAI-psychologist.git
cd GENAI-psychologist
```

#### 2. Backend Setup (FastAPI)

```bash
# Navigate to backend directory
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create .env file for environment variables
# Add your API keys and configuration
cp .env.example .env  # Create .env file with your settings
```

#### 3. Frontend Setup (Next.js)

```bash
# Navigate to frontend directory
cd aimentalhealth

# Install dependencies
npm install
# or
yarn install

# Create environment variables file if needed
# Add any required environment variables
```

### 🏃‍♂️ Running the Application

#### Start the Backend Server

```bash
# In the backend directory
cd backend

# Activate virtual environment (if not already activated)
venv\Scripts\activate  # Windows
# or
source venv/bin/activate  # macOS/Linux

# Start FastAPI server
python app.py
# or
uvicorn app:app --reload

# Server will start at http://localhost:8000
```

#### Start the Frontend Development Server

```bash
# In the frontend directory
cd aimentalhealth

# Start Next.js development server
npm run dev
# or
yarn dev

# Application will be available at http://localhost:3000
```

#### Production Build

```bash
# Frontend production build
cd aimentalhealth
npm run build
npm start

# Backend production
cd backend
# Use a production WSGI server like Gunicorn
pip install gunicorn
gunicorn app:app -w 4 -k uvicorn.workers.UvicornWorker
```

## 📱 Screenshots

### Main Interface
![Main Interface](https://github.com/salmansajidsattar/GENAI-Psychologist/blob/main/img/Screenshot%202025-09-01%20004711.png)

### Chat Interface
![Chat Interface](https://github.com/salmansajidsattar/GENAI-Psychologist/blob/main/img/Screenshot%202025-09-01%20004847.png)

## 🎥 Demo Video

Watch our demo video to see GENAI Psychologist in action:

[![GENAI Psychologist Demo](https://github.com/salmansajidsattar/GENAI-Psychologist/blob/main/Vid/Recording%202025-09-01%20005504.mp4)

*Click the image above to watch the demo video*

## 🔧 Configuration

### Backend Configuration

Create a `.env` file in the backend directory:

```env
# API Configuration
API_KEY=your_ai_api_key_here
MODEL_NAME=your_model_name
MAX_TOKENS=2048
TEMPERATURE=0.7

# Server Configuration
HOST=localhost
PORT=8000
DEBUG=True

# Security
SECRET_KEY=your_secret_key_here
```

### Frontend Configuration

Create a `.env.local` file in the frontend directory if needed:

```env
NEXT_PUBLIC_API_URL=http://localhost:8000
NEXT_PUBLIC_APP_NAME=GENAI Psychologist
```

## 🤝 Contributing

We welcome contributions to GENAI Psychologist! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⚠️ Disclaimer

GENAI Psychologist is designed to provide supportive conversations and mental health resources. It is not a replacement for professional medical advice, diagnosis, or treatment. Always seek the advice of qualified health providers with any questions you may have regarding a medical condition.

## 📞 Support

If you encounter any issues or have questions:

- 📧 Email: salmansajidsattar@gmail.com

## 🙏 Acknowledgments

- Thanks to all contributors who have helped build this project
- Inspired by the need for accessible mental health support
- Built with love for the mental health community

---

**Made with ❤️ for mental wellness**
