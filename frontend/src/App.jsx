import React, { useState, useEffect, useRef } from 'react';

const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000/api';

// SVG Vector Icons
const DiamondIcon = () => (
  <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round" className="brand-logo">
    <path d="M6 3h12l4 6-10 13L2 9z" />
    <path d="M11 3 8 9l4 13 4-13-3-6" />
    <path d="M2 9h20" />
  </svg>
);

const DashboardIcon = () => (
  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
    <rect width="7" height="9" x="3" y="3" rx="1" />
    <rect width="7" height="5" x="14" y="3" rx="1" />
    <rect width="7" height="9" x="14" y="12" rx="1" />
    <rect width="7" height="5" x="3" y="16" rx="1" />
  </svg>
);

const TransactionsIcon = () => (
  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
    <rect width="20" height="14" x="2" y="5" rx="2" />
    <line x1="2" x2="22" y1="10" y2="10" />
    <path d="M16 14h.01M12 14h.01M8 14h.01" />
  </svg>
);

const BudgetsIcon = () => (
  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
    <path d="M4 19.5v-15A2.5 2.5 0 0 1 6.5 2H20v20H6.5a2.5 2.5 0 0 1-2.5-2.5Z" />
    <path d="M6 6h10" />
    <path d="M6 10h10" />
  </svg>
);

const GoalsIcon = () => (
  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
    <circle cx="12" cy="12" r="10" />
    <circle cx="12" cy="12" r="6" />
    <circle cx="12" cy="12" r="2" />
  </svg>
);

const RiskProfileIcon = () => (
  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
    <path d="M19 21v-2a4 4 0 0 0-4-4H9a4 4 0 0 0-4 4v2" />
    <circle cx="12" cy="7" r="4" />
  </svg>
);

const LogoutIcon = () => (
  <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
    <path d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4" />
    <polyline points="16 17 21 12 16 7" />
    <line x1="21" x2="9" y1="12" y2="12" />
  </svg>
);

const SparklesIcon = () => (
  <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
    <path d="m12 3-1.912 5.813a2 2 0 0 1-1.275 1.275L3 12l5.813 1.912a2 2 0 0 1 1.275 1.275L12 21l1.912-5.813a2 2 0 0 1 1.275-1.275L21 12l-5.813-1.912a2 2 0 0 1-1.275-1.275L12 3Z" />
  </svg>
);

const ChatIcon = () => (
  <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
    <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z" />
  </svg>
);

const TrashIcon = () => (
  <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" style={{ color: 'var(--accent-rose)' }}>
    <path d="M3 6h18" />
    <path d="M19 6v14c0 1-1 2-2 2H7c-1 0-2-1-2-2V6" />
    <path d="M8 6V4c0-1 1-2 2-2h4c1 0 2 1 2 2v2" />
  </svg>
);

const EditIcon = () => (
  <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" style={{ display: 'inline', marginRight: '4px', verticalAlign: 'middle' }}>
    <path d="M12 20h9" />
    <path d="M16.5 3.5a2.12 2.12 0 0 1 3 3L7 19l-4 1 1-4Z" />
  </svg>
);

const UploadIcon = () => (
  <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" style={{ display: 'inline', marginRight: '6px' }}>
    <path d="M4 14.899A7 7 0 1 1 15.71 8h1.79a4.5 4.5 0 0 1 2.5 8.242" />
    <path d="M12 12v9" />
    <path d="m16 16-4-4-4 4" />
  </svg>
);

const TrendingUpIcon = () => (
  <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" style={{ color: 'var(--primary)' }}>
    <polyline points="22 7 13.5 15.5 8.5 10.5 2 17" />
    <polyline points="16 7 22 7 22 13" />
  </svg>
);

export default function App() {
  // Authentication State
  const [token, setToken] = useState(localStorage.getItem('token') || '');
  const [email, setEmail] = useState(localStorage.getItem('email') || '');
  const [isLoginView, setIsLoginView] = useState(true);
  const [authEmail, setAuthEmail] = useState('');
  const [authPassword, setAuthPassword] = useState('');

  // Main UI State
  const [activeTab, setActiveTab] = useState('dashboard');
  const [isChatOpen, setIsChatOpen] = useState(false);
  const [toast, setToast] = useState({ message: '', type: '' });

  // Core Financial Data
  const [transactions, setTransactions] = useState([]);
  const [budgets, setBudgets] = useState([]);
  const [goals, setGoals] = useState([]);
  const [profile, setProfile] = useState({ annual_income: 0, risk_tolerance: 'Medium', investment_experience: 'None', age: 30 });
  const [advisorReport, setAdvisorReport] = useState('');
  const [isCompiling, setIsCompiling] = useState(false);

  // Chat State
  const [chatMessages, setChatMessages] = useState([
    { sender: 'ai', text: 'Hello! I am your AI Wealth Advisor. I have analyzed your transactions and set up recommendations. What financial questions can I answer for you today?', timestamp: new Date().toISOString() }
  ]);
  const [chatInput, setChatInput] = useState('');
  const [isChatLoading, setIsChatLoading] = useState(false);

  // Form states for creating new items
  const [newTx, setNewTx] = useState({ amount: '', category: 'Dining Out', date: new Date().toISOString().split('T')[0], type: 'expense', description: '' });
  const [newBudget, setNewBudget] = useState({ category: 'Dining Out', limit_amount: '' });
  const [newGoal, setNewGoal] = useState({ name: '', target_amount: '', current_amount: '0', target_date: '' });

  // File Upload State
  const fileInputRef = useRef(null);

  // Show visual alerts
  const showToast = (message, type = 'success') => {
    setToast({ message, type });
    setTimeout(() => setToast({ message: '', type: '' }), 4000);
  };

  // Auth fetch wrapper
  const apiFetch = async (endpoint, options = {}) => {
    const headers = {
      ...options.headers,
    };
    if (token) {
      headers['Authorization'] = `Bearer ${token}`;
    }
    if (!(options.body instanceof FormData) && options.body) {
      headers['Content-Type'] = 'application/json';
    }

    try {
      const response = await fetch(`${API_BASE_URL}${endpoint}`, {
        ...options,
        headers,
      });

      if (response.status === 401) {
        handleLogout();
        throw new Error('Session expired. Please log in again.');
      }

      if (!response.ok) {
        const errData = await response.json().catch(() => ({}));
        throw new Error(errData.detail || 'An error occurred.');
      }

      if (response.status === 204) return null;
      return await response.json();
    } catch (error) {
      console.error(`API Fetch Error (${endpoint}):`, error);
      throw error;
    }
  };

  // Auth Handlers
  const handleAuth = async (e) => {
    e.preventDefault();
    if (!authEmail || !authPassword) return;

    try {
      if (isLoginView) {
        const formData = new FormData();
        formData.append('username', authEmail);
        formData.append('password', authPassword);

        const data = await apiFetch('/auth/login', {
          method: 'POST',
          body: formData,
        });

        localStorage.setItem('token', data.access_token);
        localStorage.setItem('email', authEmail);
        setToken(data.access_token);
        setEmail(authEmail);
        showToast('Successfully logged in!', 'success');
      } else {
        await apiFetch('/auth/register', {
          method: 'POST',
          body: JSON.stringify({ email: authEmail, password: authPassword }),
        });
        showToast('Registration successful! Please login.', 'success');
        setIsLoginView(true);
        setAuthPassword('');
      }
    } catch (err) {
      showToast(err.message, 'error');
    }
  };

  const handleLogout = () => {
    localStorage.removeItem('token');
    localStorage.removeItem('email');
    setToken('');
    setEmail('');
    setTransactions([]);
    setBudgets([]);
    setGoals([]);
    setAdvisorReport('');
    showToast('Logged out successfully.', 'success');
  };

  // Synchronize financial data
  const fetchData = async () => {
    if (!token) return;
    try {
      const txData = await apiFetch('/transactions');
      setTransactions(txData);

      const bdgData = await apiFetch('/budgets');
      setBudgets(bdgData);

      const goalData = await apiFetch('/goals');
      setGoals(goalData);

      const profileData = await apiFetch('/profile');
      setProfile(profileData);
    } catch (err) {
      showToast(err.message, 'error');
    }
  };

  useEffect(() => {
    if (token) {
      fetchData();
    }
  }, [token]);

  // Run LangGraph compiler to get overall advisory report
  const compileAdvisory = async () => {
    setIsCompiling(true);
    try {
      const data = await apiFetch('/advisor/compile', { method: 'POST' });
      setAdvisorReport(data.reply);
      showToast('AI Advisory Report compiled!', 'success');
      fetchData();
    } catch (err) {
      showToast('Failed to compile advice: ' + err.message, 'error');
    } finally {
      setIsCompiling(false);
    }
  };

  // Chat Advisor handler
  const sendChatMessage = async (e) => {
    e.preventDefault();
    if (!chatInput.trim()) return;

    const userMsg = { sender: 'user', text: chatInput, timestamp: new Date().toISOString() };
    setChatMessages((prev) => [...prev, userMsg]);
    setChatInput('');
    setIsChatLoading(true);

    try {
      const response = await apiFetch('/advisor/chat', {
        method: 'POST',
        body: JSON.stringify({
          message: userMsg.text,
          history: chatMessages
        }),
      });

      setChatMessages((prev) => [...prev, { sender: 'ai', text: response.reply, timestamp: new Date().toISOString() }]);
    } catch (err) {
      showToast(err.message, 'error');
    } finally {
      setIsChatLoading(false);
    }
  };

  // CRUD actions: Transactions
  const addTransaction = async (e) => {
    e.preventDefault();
    try {
      const added = await apiFetch('/transactions', {
        method: 'POST',
        body: JSON.stringify({
          amount: parseFloat(newTx.amount),
          category: newTx.category,
          date: newTx.date,
          type: newTx.type,
          description: newTx.description || 'Transaction'
        }),
      });
      setTransactions((prev) => [added, ...prev]);
      setNewTx({ amount: '', category: 'Dining Out', date: new Date().toISOString().split('T')[0], type: 'expense', description: '' });
      showToast('Transaction added!');
      compileAdvisory();
    } catch (err) {
      showToast(err.message, 'error');
    }
  };

  const deleteTransaction = async (id) => {
    try {
      await apiFetch(`/transactions/${id}`, { method: 'DELETE' });
      setTransactions((prev) => prev.filter((t) => t.id !== id));
      showToast('Transaction deleted.');
      compileAdvisory();
    } catch (err) {
      showToast(err.message, 'error');
    }
  };

  // CSV Upload handler
  const handleCSVUpload = async (e) => {
    const file = e.target.files[0];
    if (!file) return;

    const formData = new FormData();
    formData.append('file', file);

    try {
      const res = await apiFetch('/transactions/upload', {
        method: 'POST',
        body: formData,
      });
      showToast(`Success! Imported ${res.imported} transactions.`, 'success');
      fetchData();
      compileAdvisory();
    } catch (err) {
      showToast('CSV parsing failed: ' + err.message, 'error');
    }
  };

  // CRUD actions: Budgets
  const saveBudget = async (e) => {
    e.preventDefault();
    try {
      const added = await apiFetch('/budgets', {
        method: 'POST',
        body: JSON.stringify({
          category: newBudget.category,
          limit_amount: parseFloat(newBudget.limit_amount),
        }),
      });
      setBudgets((prev) => {
        const filtered = prev.filter((b) => b.category !== added.category);
        return [...filtered, added];
      });
      setNewBudget({ category: 'Dining Out', limit_amount: '' });
      showToast('Budget saved!');
      compileAdvisory();
    } catch (err) {
      showToast(err.message, 'error');
    }
  };

  const deleteBudget = async (id) => {
    try {
      await apiFetch(`/budgets/${id}`, { method: 'DELETE' });
      setBudgets((prev) => prev.filter((b) => b.id !== id));
      showToast('Budget deleted.');
      compileAdvisory();
    } catch (err) {
      showToast(err.message, 'error');
    }
  };

  // CRUD actions: Goals
  const addGoal = async (e) => {
    e.preventDefault();
    try {
      const added = await apiFetch('/goals', {
        method: 'POST',
        body: JSON.stringify({
          name: newGoal.name,
          target_amount: parseFloat(newGoal.target_amount),
          current_amount: parseFloat(newGoal.current_amount || 0),
          target_date: newGoal.target_date,
        }),
      });
      setGoals((prev) => [...prev, added]);
      setNewGoal({ name: '', target_amount: '', current_amount: '0', target_date: '' });
      showToast('Financial goal set!');
      compileAdvisory();
    } catch (err) {
      showToast(err.message, 'error');
    }
  };

  const updateGoalProgress = async (id, amount) => {
    try {
      const updated = await apiFetch(`/goals/${id}`, {
        method: 'PUT',
        body: JSON.stringify({ current_amount: parseFloat(amount) }),
      });
      setGoals((prev) => prev.map((g) => (g.id === id ? updated : g)));
      showToast('Goal progress updated!');
      compileAdvisory();
    } catch (err) {
      showToast(err.message, 'error');
    }
  };

  const deleteGoal = async (id) => {
    try {
      await apiFetch(`/goals/${id}`, { method: 'DELETE' });
      setGoals((prev) => prev.filter((g) => g.id !== id));
      showToast('Goal removed.');
      compileAdvisory();
    } catch (err) {
      showToast(err.message, 'error');
    }
  };

  // Profile save
  const saveProfile = async (e) => {
    e.preventDefault();
    try {
      const updated = await apiFetch('/profile', {
        method: 'POST',
        body: JSON.stringify(profile),
      });
      setProfile(updated);
      showToast('Risk profile updated successfully!');
      compileAdvisory();
    } catch (err) {
      showToast(err.message, 'error');
    }
  };

  // Chart computations
  const totalIncome = transactions
    .filter((t) => t.type === 'income')
    .reduce((sum, t) => sum + t.amount, 0);

  const totalExpense = transactions
    .filter((t) => t.type === 'expense')
    .reduce((sum, t) => sum + t.amount, 0);

  const netSavings = totalIncome - totalExpense;
  const savingsRate = totalIncome > 0 ? (netSavings / totalIncome) * 100 : 0;

  // Group expenses by category
  const expenseCategories = {};
  transactions
    .filter((t) => t.type === 'expense')
    .forEach((t) => {
      expenseCategories[t.category] = (expenseCategories[t.category] || 0) + t.amount;
    });

  const maxCategoryValue = Math.max(...Object.values(expenseCategories), 100);

  // Markdown parsing utility
  const parseMarkdown = (md) => {
    if (!md) return '';
    let html = md;
    
    // Parse tables
    const lines = html.split('\n');
    let inTable = false;
    let tableHtml = '';
    const processedLines = [];
    
    for (let i = 0; i < lines.length; i++) {
      const line = lines[i].trim();
      if (line.startsWith('|') && line.endsWith('|')) {
        if (!inTable) {
          inTable = true;
          tableHtml = '<table><thead>';
        }
        
        const cells = line.split('|').slice(1, -1).map(c => c.trim());
        
        // Separator row check
        if (cells.every(c => /^:-*|-*:-*|-*:$/.test(c))) {
          tableHtml = tableHtml.replace('</table><thead>', '</thead><tbody>');
          continue;
        }
        
        const isHeader = tableHtml.includes('<thead>') && !tableHtml.includes('</thead>');
        const cellTag = isHeader ? 'th' : 'td';
        
        tableHtml += 'tr';
        cells.forEach(cell => {
          tableHtml += `<${cellTag}>${cell}</${cellTag}>`;
        });
        tableHtml += '</tr>';
      } else {
        if (inTable) {
          inTable = false;
          tableHtml += '</tbody></table>';
          processedLines.push(tableHtml);
          tableHtml = '';
        }
        processedLines.push(lines[i]);
      }
    }
    if (inTable) {
      tableHtml += '</tbody></table>';
      processedLines.push(tableHtml);
    }
    
    html = processedLines.join('\n');

    // Headers
    html = html.replace(/^### (.*$)/gim, '<h4>$1</h4>');
    html = html.replace(/^## (.*$)/gim, '<h3>$1</h3>');
    html = html.replace(/^# (.*$)/gim, '<h2>$1</h2>');
    
    // Bold
    html = html.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>');
    
    // Alerts/Quotes
    html = html.replace(/^> \[\!(NOTE|TIP|IMPORTANT|WARNING|CAUTION)\]\s*(.*$)/gim, '<blockquote><strong>$1</strong>: $2');
    html = html.replace(/^> (.*$)/gim, '<blockquote>$2</blockquote>');
    
    // Lists
    let inList = false;
    const listProcessed = [];
    const listLines = html.split('\n');
    for (let i = 0; i < listLines.length; i++) {
      const line = listLines[i];
      const match = line.match(/^[-*]\s+(.*)$/);
      if (match) {
        if (!inList) {
          inList = true;
          listProcessed.push('<ul>');
        }
        listProcessed.push(`<li>${match[1]}</li>`);
      } else {
        if (inList) {
          inList = false;
          listProcessed.push('</ul>');
        }
        listProcessed.push(line);
      }
    }
    if (inList) {
      listProcessed.push('</ul>');
    }
    html = listProcessed.join('\n');
    
    // Paragraph spacing
    html = html.replace(/\n\n/g, '<br />');

    return html;
  };

  // Authentication View
  if (!token) {
    return (
      <div className="min-h-screen bg-slate-50 flex items-center justify-center p-4 font-sans text-slate-900">
        <div className="bg-white p-8 rounded-2xl shadow-floating max-w-md w-full border border-slate-200">
          <div className="text-center mb-8">
            <span className="inline-block text-slate-900 mb-4">
              <DiamondIcon />
            </span>
            <h2 className="text-3xl font-extrabold text-slate-900 tracking-tight">AuraWealth</h2>
            <p className="text-slate-500 mt-2 text-sm">
              {isLoginView ? 'Sign in to access your wealth dashboard.' : 'Create an account to start wealth planning.'}
            </p>
          </div>
          <form onSubmit={handleAuth} className="space-y-6">
            <div>
              <label className="block text-sm font-semibold text-slate-700 mb-2">Email Address</label>
              <input
                type="email"
                className="w-full bg-slate-50 border border-slate-200 text-slate-900 rounded-lg px-4 py-3 focus:bg-white focus:ring-2 focus:ring-slate-900 focus:border-slate-900 outline-none transition-all text-sm"
                placeholder="you@example.com"
                value={authEmail}
                onChange={(e) => setAuthEmail(e.target.value)}
                required
              />
            </div>
            <div>
              <label className="block text-sm font-semibold text-slate-700 mb-2">Password</label>
              <input
                type="password"
                className="w-full bg-slate-50 border border-slate-200 text-slate-900 rounded-lg px-4 py-3 focus:bg-white focus:ring-2 focus:ring-slate-900 focus:border-slate-900 outline-none transition-all text-sm"
                placeholder="••••••••"
                value={authPassword}
                onChange={(e) => setAuthPassword(e.target.value)}
                required
              />
            </div>
            <button type="submit" className="w-full bg-slate-900 text-white rounded-lg px-4 py-3 text-sm font-bold tracking-wide hover:bg-slate-800 transition-colors shadow-md">
              {isLoginView ? 'Access Account' : 'Open Account'}
            </button>
          </form>
          <div className="mt-8 text-center text-sm text-slate-500">
            {isLoginView ? (
              <p>New to AuraWealth? <span className="text-slate-900 font-bold cursor-pointer hover:underline" onClick={() => setIsLoginView(false)}>Apply Now</span></p>
            ) : (
              <p>Already a client? <span className="text-slate-900 font-bold cursor-pointer hover:underline" onClick={() => setIsLoginView(true)}>Sign In</span></p>
            )}
          </div>
        </div>
        {toast.message && (
          <div className={`fixed bottom-6 right-6 px-6 py-4 rounded-xl shadow-floating text-sm font-bold text-white ${toast.type === 'error' ? 'bg-rose-600' : 'bg-emerald-600'}`}>
            {toast.message}
          </div>
        )}
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-slate-50 flex font-sans text-slate-900 overflow-hidden">
      {/* Premium Dark Sidebar */}
      <aside className="w-72 bg-slate-900 border-r border-slate-800 flex flex-col justify-between h-screen shrink-0 relative z-20 shadow-2xl">
        <div>
          <div className="p-8 flex items-center gap-4 border-b border-slate-800">
            <span className="text-white"><DiamondIcon /></span>
            <span className="font-extrabold text-xl tracking-tight text-white">AuraWealth</span>
          </div>
          <div className="px-4 py-6 space-y-2">
            <div className="text-[10px] font-bold text-slate-500 uppercase tracking-widest px-4 mb-4">Platform</div>
            
            <li className={`flex items-center gap-4 px-4 py-3 rounded-lg cursor-pointer transition-all duration-300 list-none ${activeTab === 'dashboard' ? 'bg-slate-800 text-white font-semibold border-l-2 border-blue-500' : 'text-slate-400 hover:bg-slate-800/50 hover:text-slate-200'}`} onClick={() => setActiveTab('dashboard')}>
              <DashboardIcon /> <span className="text-sm tracking-wide">Dashboard</span>
            </li>
            <li className={`flex items-center gap-4 px-4 py-3 rounded-lg cursor-pointer transition-all duration-300 list-none ${activeTab === 'transactions' ? 'bg-slate-800 text-white font-semibold border-l-2 border-blue-500' : 'text-slate-400 hover:bg-slate-800/50 hover:text-slate-200'}`} onClick={() => setActiveTab('transactions')}>
              <TransactionsIcon /> <span className="text-sm tracking-wide">Transactions</span>
            </li>
            <li className={`flex items-center gap-4 px-4 py-3 rounded-lg cursor-pointer transition-all duration-300 list-none ${activeTab === 'budgets' ? 'bg-slate-800 text-white font-semibold border-l-2 border-blue-500' : 'text-slate-400 hover:bg-slate-800/50 hover:text-slate-200'}`} onClick={() => setActiveTab('budgets')}>
              <BudgetsIcon /> <span className="text-sm tracking-wide">Budgets</span>
            </li>
            <li className={`flex items-center gap-4 px-4 py-3 rounded-lg cursor-pointer transition-all duration-300 list-none ${activeTab === 'goals' ? 'bg-slate-800 text-white font-semibold border-l-2 border-blue-500' : 'text-slate-400 hover:bg-slate-800/50 hover:text-slate-200'}`} onClick={() => setActiveTab('goals')}>
              <GoalsIcon /> <span className="text-sm tracking-wide">Goals</span>
            </li>
            <div className="text-[10px] font-bold text-slate-500 uppercase tracking-widest px-4 mt-8 mb-4">Advisory</div>
            <li className={`flex items-center gap-4 px-4 py-3 rounded-lg cursor-pointer transition-all duration-300 list-none ${activeTab === 'profile' ? 'bg-slate-800 text-white font-semibold border-l-2 border-blue-500' : 'text-slate-400 hover:bg-slate-800/50 hover:text-slate-200'}`} onClick={() => setActiveTab('profile')}>
              <RiskProfileIcon /> <span className="text-sm tracking-wide">Risk Profile</span>
            </li>
          </div>
        </div>
        <div className="p-4 m-6 bg-slate-800 rounded-xl border border-slate-700 flex items-center justify-between hover:bg-slate-700 transition-colors cursor-default">
          <div className="flex items-center gap-3 overflow-hidden">
            <div className="w-10 h-10 rounded-full bg-slate-700 text-white font-bold flex items-center justify-center text-sm shrink-0 border border-slate-600">{email.charAt(0).toUpperCase()}</div>
            <div className="overflow-hidden">
              <div className="text-sm font-bold text-white truncate">{email}</div>
              <div className="text-[10px] text-emerald-400 uppercase tracking-widest font-bold mt-1">Aura Pro</div>
            </div>
          </div>
          <button className="text-slate-400 hover:text-rose-500 transition-colors p-2 rounded-lg hover:bg-slate-800" onClick={handleLogout} title="Sign Out">
            <LogoutIcon />
          </button>
        </div>
      </aside>

      {/* Main View Area */}
      <main className="flex-1 h-screen overflow-y-auto p-8 lg:p-12 scroll-smooth relative z-10">
        <header className="flex flex-col md:flex-row md:items-end justify-between mb-10 gap-6">
          <div>
            <h1 className="text-4xl font-extrabold text-slate-900 tracking-tight">{activeTab.charAt(0).toUpperCase() + activeTab.slice(1)}</h1>
            <p className="text-slate-500 text-sm mt-2 font-medium">Welcome back. Here is your aggregated wealth summary.</p>
          </div>
          <div className="flex items-center gap-4">
            <button onClick={compileAdvisory} disabled={isCompiling} className="flex items-center gap-2 px-5 py-2.5 bg-white border border-slate-200 rounded-lg shadow-sm text-sm font-bold text-slate-700 hover:bg-slate-50 hover:border-slate-300 transition-all disabled:opacity-50">
              <SparklesIcon /> {isCompiling ? 'Analyzing...' : 'Sync AI Advice'}
            </button>
            <button onClick={() => setIsChatOpen(!isChatOpen)} className="flex items-center gap-2 px-5 py-2.5 bg-blue-600 text-white rounded-lg shadow-sm text-sm font-bold hover:bg-blue-700 transition-all hover:shadow-md">
              <ChatIcon /> {isChatOpen ? 'Close Assistant' : 'Ask AI Advisor'}
            </button>
          </div>
        </header>

        {toast.message && (
          <div className={`fixed bottom-6 right-6 px-6 py-4 rounded-xl shadow-floating text-sm font-bold text-white z-50 ${toast.type === 'error' ? 'bg-rose-600' : 'bg-emerald-600'}`}>
            {toast.message}
          </div>
        )}

        {activeTab === 'dashboard' && (
          <div className="space-y-8">
            <div className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-4 gap-6">
              <div className="bg-white rounded-2xl shadow-sm border border-slate-200 p-6 flex flex-col justify-between hover:shadow-md hover:-translate-y-1 transition-all duration-300 relative overflow-hidden group">
                <div className="absolute top-0 right-0 w-24 h-24 bg-emerald-50 rounded-bl-full -mr-4 -mt-4 transition-transform group-hover:scale-110"></div>
                <div className="text-[11px] font-bold text-slate-500 uppercase tracking-widest mb-4 relative z-10">Monthly Inflows</div>
                <div className="text-4xl font-extrabold text-slate-900 tabular-nums mb-3 tracking-tight relative z-10">${totalIncome.toLocaleString(undefined, { minimumFractionDigits: 2, maximumFractionDigits: 2 })}</div>
                <div className="text-[11px] font-bold inline-flex items-center px-2.5 py-1 rounded-md w-max bg-emerald-50 text-emerald-600 relative z-10"><TrendingUpIcon /> Active Payroll</div>
              </div>
              <div className="bg-white rounded-2xl shadow-sm border border-slate-200 p-6 flex flex-col justify-between hover:shadow-md hover:-translate-y-1 transition-all duration-300 relative overflow-hidden group">
                <div className="absolute top-0 right-0 w-24 h-24 bg-rose-50 rounded-bl-full -mr-4 -mt-4 transition-transform group-hover:scale-110"></div>
                <div className="text-[11px] font-bold text-slate-500 uppercase tracking-widest mb-4 relative z-10">Monthly Spending</div>
                <div className="text-4xl font-extrabold text-slate-900 tabular-nums mb-3 tracking-tight relative z-10">${totalExpense.toLocaleString(undefined, { minimumFractionDigits: 2, maximumFractionDigits: 2 })}</div>
                <div className="text-[11px] font-bold inline-flex items-center px-2.5 py-1 rounded-md w-max bg-rose-50 text-rose-600 relative z-10">Capital outflows</div>
              </div>
              <div className="bg-white rounded-2xl shadow-sm border border-slate-200 p-6 flex flex-col justify-between hover:shadow-md hover:-translate-y-1 transition-all duration-300 relative overflow-hidden group">
                <div className="absolute top-0 right-0 w-24 h-24 bg-blue-50 rounded-bl-full -mr-4 -mt-4 transition-transform group-hover:scale-110"></div>
                <div className="text-[11px] font-bold text-slate-500 uppercase tracking-widest mb-4 relative z-10">Net Savings</div>
                <div className="text-4xl font-extrabold text-slate-900 tabular-nums mb-3 tracking-tight relative z-10">${netSavings.toLocaleString(undefined, { minimumFractionDigits: 2, maximumFractionDigits: 2 })}</div>
                <div className="text-[11px] font-bold inline-flex items-center px-2.5 py-1 rounded-md w-max bg-blue-50 text-blue-600 relative z-10">Surplus margin</div>
              </div>
              <div className="bg-white rounded-2xl shadow-sm border border-slate-200 p-6 flex flex-col justify-between hover:shadow-md hover:-translate-y-1 transition-all duration-300 relative overflow-hidden group">
                <div className="absolute top-0 right-0 w-24 h-24 bg-slate-50 rounded-bl-full -mr-4 -mt-4 transition-transform group-hover:scale-110"></div>
                <div className="text-[11px] font-bold text-slate-500 uppercase tracking-widest mb-4 relative z-10">Savings Velocity</div>
                <div className="text-4xl font-extrabold text-slate-900 tabular-nums mb-3 tracking-tight relative z-10">{savingsRate.toFixed(1)}%</div>
                <div className={`text-[11px] font-bold inline-flex items-center px-2.5 py-1 rounded-md w-max relative z-10 ${savingsRate >= 20 ? 'bg-emerald-50 text-emerald-600' : 'bg-amber-50 text-amber-600'}`}>
                  Target benchmark: 20%
                </div>
              </div>
            </div>

            <div className="grid grid-cols-1 xl:grid-cols-3 gap-8">
              <div className="xl:col-span-2 bg-white rounded-2xl shadow-sm border border-slate-200 p-8">
                <div className="text-lg font-extrabold text-slate-900 mb-8 tracking-tight">Expense Analytics</div>
                {Object.keys(expenseCategories).length === 0 ? (
                  <div className="flex flex-col items-center justify-center py-16 text-slate-400">
                    <p className="text-sm font-medium">No expense transactions recorded.</p>
                  </div>
                ) : (
                  <div className="flex items-end gap-3 mt-4" style={{ height: '248px' }}>
                    {Object.entries(expenseCategories).map(([cat, val], idx) => {
                      const palette = ['#3B82F6','#6366F1','#8B5CF6','#A855F7','#EC4899','#F43F5E','#14B8A6'];
                      const barColor = palette[idx % palette.length];
                      const barHeight = Math.max((val / maxCategoryValue) * 200, 8);
                      const label = val >= 1000 ? (val / 1000).toFixed(1) + 'k' : val.toFixed(0);
                      return (
                        <div className="flex-1 flex flex-col justify-end items-center group" key={cat}>
                          <div className="text-[10px] font-bold text-slate-600 mb-1.5 tabular-nums opacity-80 group-hover:opacity-100 transition-opacity">
                            {'$'}{label}
                          </div>
                          <div
                            className="w-full rounded-t-md shadow-sm cursor-default"
                            style={{
                              height: barHeight + 'px',
                              backgroundColor: barColor,
                              transition: 'height 0.6s cubic-bezier(0.34, 1.56, 0.64, 1), opacity 0.3s ease',
                              opacity: 0.85,
                            }}
                            onMouseEnter={(e) => { e.currentTarget.style.opacity = '1'; }}
                            onMouseLeave={(e) => { e.currentTarget.style.opacity = '0.85'; }}
                          />
                          <div className="text-[9px] font-semibold text-slate-400 text-center mt-2 truncate w-full leading-tight">
                            {cat}
                          </div>
                        </div>
                      );
                    })}
                  </div>
                )}
              </div>

              <div className="bg-white rounded-2xl shadow-sm border border-slate-200 p-8 flex flex-col">
                <div className="text-lg font-extrabold text-slate-900 mb-8 tracking-tight">Advisory Status</div>
                <div className="space-y-6 flex-1">
                  <div className="bg-slate-50 p-5 rounded-xl border border-slate-200">
                    <div className="text-[11px] text-slate-500 font-bold uppercase tracking-widest mb-2">Asset Risk Profile</div>
                    <div className="text-xl font-extrabold text-slate-900">{profile.risk_tolerance} Allocation</div>
                  </div>
                  <div className="bg-slate-50 p-5 rounded-xl border border-slate-200">
                    <div className="text-[11px] text-slate-500 font-bold uppercase tracking-widest mb-2">Budget Compliance</div>
                    <div className="text-xl font-extrabold text-emerald-600">
                      {budgets.length > 0 ? `${budgets.length} Monitored` : 'No Budgets'}
                    </div>
                  </div>
                </div>
                <button onClick={() => setActiveTab('profile')} className="mt-6 w-full px-4 py-3 bg-white border border-slate-300 rounded-lg shadow-sm text-sm font-bold text-slate-700 hover:bg-slate-50 transition-colors">
                  Review Risk Settings
                </button>
              </div>
            </div>

            <div className="bg-white rounded-2xl shadow-sm border border-slate-200 p-8">
              <div className="flex items-center justify-between mb-8 border-b border-slate-100 pb-6">
                <div className="flex items-center gap-3">
                  <span className="text-slate-900"><SparklesIcon /></span>
                  <h3 className="text-xl font-extrabold text-slate-900 tracking-tight">Wealth Advisory Report</h3>
                </div>
                <span className="text-xs font-bold uppercase tracking-widest text-slate-400">AI Synthesis</span>
              </div>
              {advisorReport ? (
                <div className="prose prose-slate max-w-none prose-headings:font-extrabold prose-h3:text-lg prose-p:text-slate-600 prose-p:leading-relaxed prose-a:text-blue-600 prose-li:text-slate-600" dangerouslySetInnerHTML={{ __html: parseMarkdown(advisorReport) }} />
              ) : (
                <div className="text-center py-16">
                  <p className="text-slate-500 text-sm font-medium mb-6">No advisory report compiled. Trigger the intelligence engine to synthesize your data.</p>
                  <button onClick={compileAdvisory} className="px-6 py-3 bg-slate-900 text-white rounded-lg shadow-md text-sm font-bold hover:bg-slate-800 transition-colors" disabled={isCompiling}>
                    {isCompiling ? 'Engine Running...' : 'Generate Wealth Report'}
                  </button>
                </div>
              )}
            </div>
          </div>
        )}

        {activeTab === 'transactions' && (
          <div className="grid grid-cols-1 xl:grid-cols-3 gap-8">
            <div className="xl:col-span-1 space-y-8">
              <div className="bg-white rounded-2xl shadow-sm border border-slate-200 p-8">
                <div className="text-lg font-extrabold text-slate-900 mb-6 tracking-tight">Record Transaction</div>
                <form onSubmit={addTransaction} className="space-y-5">
                  <div>
                    <label className="block text-[11px] font-bold text-slate-500 mb-2 uppercase tracking-widest">Type</label>
                    <select className="w-full bg-slate-50 border border-slate-200 text-slate-900 rounded-lg px-4 py-2.5 focus:bg-white focus:ring-2 focus:ring-slate-900 outline-none transition-all text-sm font-medium" value={newTx.type} onChange={(e) => setNewTx({ ...newTx, type: e.target.value })}>
                      <option value="expense">Expense (Outflow)</option>
                      <option value="income">Income (Inflow)</option>
                    </select>
                  </div>
                  <div>
                    <label className="block text-[11px] font-bold text-slate-500 mb-2 uppercase tracking-widest">Amount ($)</label>
                    <input type="number" step="0.01" className="w-full bg-slate-50 border border-slate-200 text-slate-900 rounded-lg px-4 py-2.5 focus:bg-white focus:ring-2 focus:ring-slate-900 outline-none transition-all text-sm tabular-nums font-bold" placeholder="0.00" value={newTx.amount} onChange={(e) => setNewTx({ ...newTx, amount: e.target.value })} required />
                  </div>
                  <div>
                    <label className="block text-[11px] font-bold text-slate-500 mb-2 uppercase tracking-widest">Category</label>
                    <select className="w-full bg-slate-50 border border-slate-200 text-slate-900 rounded-lg px-4 py-2.5 focus:bg-white focus:ring-2 focus:ring-slate-900 outline-none transition-all text-sm font-medium" value={newTx.category} onChange={(e) => setNewTx({ ...newTx, category: e.target.value })}>
                      <option value="Housing">Housing</option>
                      <option value="Groceries">Groceries</option>
                      <option value="Dining Out">Dining Out</option>
                      <option value="Transport">Transport</option>
                      <option value="Subscriptions">Subscriptions</option>
                      <option value="Entertainment">Entertainment</option>
                      <option value="Income">Salary / Income</option>
                      <option value="Shopping">Shopping & Discretionary</option>
                    </select>
                  </div>
                  <div>
                    <label className="block text-[11px] font-bold text-slate-500 mb-2 uppercase tracking-widest">Date</label>
                    <input type="date" className="w-full bg-slate-50 border border-slate-200 text-slate-900 rounded-lg px-4 py-2.5 focus:bg-white focus:ring-2 focus:ring-slate-900 outline-none transition-all text-sm font-medium" value={newTx.date} onChange={(e) => setNewTx({ ...newTx, date: e.target.value })} required />
                  </div>
                  <div>
                    <label className="block text-[11px] font-bold text-slate-500 mb-2 uppercase tracking-widest">Description</label>
                    <input type="text" className="w-full bg-slate-50 border border-slate-200 text-slate-900 rounded-lg px-4 py-2.5 focus:bg-white focus:ring-2 focus:ring-slate-900 outline-none transition-all text-sm font-medium" placeholder="e.g. Starbucks" value={newTx.description} onChange={(e) => setNewTx({ ...newTx, description: e.target.value })} required />
                  </div>
                  <button type="submit" className="w-full bg-slate-900 text-white rounded-lg px-4 py-3 text-sm font-bold hover:bg-slate-800 transition-colors shadow-sm mt-4 tracking-wide">Record Transaction</button>
                </form>
              </div>

              <div className="bg-white rounded-2xl shadow-sm border border-slate-200 p-8">
                <div className="text-sm font-extrabold text-slate-900 mb-3 tracking-tight">Bulk Import</div>
                <p className="text-xs text-slate-500 mb-6 leading-relaxed font-medium">Upload statements. Expected columns: amount, category, date, type, description</p>
                <input type="file" accept=".csv" className="hidden" ref={fileInputRef} onChange={handleCSVUpload} />
                <button onClick={() => fileInputRef.current.click()} className="w-full flex items-center justify-center gap-2 px-4 py-3 bg-white border border-slate-200 rounded-lg shadow-sm text-sm font-bold text-slate-700 hover:bg-slate-50 transition-colors">
                  <UploadIcon /> Choose CSV File
                </button>
              </div>
            </div>

            <div className="xl:col-span-2 bg-white rounded-2xl shadow-sm border border-slate-200 overflow-hidden flex flex-col h-[calc(100vh-12rem)]">
              <div className="p-8 border-b border-slate-200 bg-white sticky top-0 z-10">
                <h3 className="text-lg font-extrabold text-slate-900 tracking-tight">Ledger</h3>
              </div>
              <div className="flex-1 overflow-y-auto">
                {transactions.length === 0 ? (
                  <div className="flex items-center justify-center h-full text-slate-400 text-sm font-medium">No ledger entries.</div>
                ) : (
                  <table className="w-full text-left border-collapse">
                    <thead className="bg-slate-50 sticky top-0 shadow-sm z-10">
                      <tr>
                        <th className="px-8 py-4 text-[10px] font-bold text-slate-500 uppercase tracking-widest whitespace-nowrap">Date & Desc</th>
                        <th className="px-8 py-4 text-[10px] font-bold text-slate-500 uppercase tracking-widest">Category</th>
                        <th className="px-8 py-4 text-[10px] font-bold text-slate-500 uppercase tracking-widest text-right">Amount</th>
                        <th className="px-8 py-4"></th>
                      </tr>
                    </thead>
                    <tbody className="divide-y divide-slate-100">
                      {transactions.map((tx) => (
                        <tr key={tx.id} className="hover:bg-slate-50 transition-colors group">
                          <td className="px-8 py-5">
                            <div className="text-sm font-bold text-slate-900">{tx.description}</div>
                            <div className="text-xs text-slate-500 mt-1 font-medium">{tx.date}</div>
                          </td>
                          <td className="px-8 py-5">
                            <span className="px-3 py-1 rounded-md text-[10px] font-bold bg-slate-100 text-slate-600 tracking-widest uppercase">{tx.category}</span>
                          </td>
                          <td className={`px-8 py-5 text-right text-[15px] font-extrabold tabular-nums tracking-tight ${tx.type === 'expense' ? 'text-slate-900' : 'text-emerald-500'}`}>
                            {tx.type === 'expense' ? '-' : '+'}${tx.amount.toFixed(2)}
                          </td>
                          <td className="px-8 py-5 text-right">
                            <button onClick={() => deleteTransaction(tx.id)} className="text-slate-300 hover:text-rose-500 transition-colors opacity-0 group-hover:opacity-100">
                              <TrashIcon />
                            </button>
                          </td>
                        </tr>
                      ))}
                    </tbody>
                  </table>
                )}
              </div>
            </div>
          </div>
        )}

        {activeTab === 'budgets' && (
          <div className="space-y-8">
            <div className="grid grid-cols-1 lg:grid-cols-4 gap-8">
              <div className="lg:col-span-1">
                <div className="bg-white rounded-2xl shadow-sm border border-slate-200 p-8 sticky top-8">
                  <div className="text-lg font-extrabold text-slate-900 mb-6 tracking-tight">Define Category Limit</div>
                  <form onSubmit={saveBudget} className="space-y-5">
                    <div>
                      <label className="block text-[11px] font-bold text-slate-500 mb-2 uppercase tracking-widest">Category</label>
                      <select className="w-full bg-slate-50 border border-slate-200 text-slate-900 rounded-lg px-4 py-2.5 focus:bg-white focus:ring-2 focus:ring-slate-900 outline-none transition-all text-sm font-medium" value={newBudget.category} onChange={(e) => setNewBudget({ ...newBudget, category: e.target.value })}>
                        <option value="Housing">Housing</option>
                        <option value="Groceries">Groceries</option>
                        <option value="Dining Out">Dining Out</option>
                        <option value="Transport">Transport</option>
                        <option value="Subscriptions">Subscriptions</option>
                        <option value="Entertainment">Entertainment</option>
                        <option value="Shopping">Shopping</option>
                      </select>
                    </div>
                    <div>
                      <label className="block text-[11px] font-bold text-slate-500 mb-2 uppercase tracking-widest">Monthly Limit ($)</label>
                      <input type="number" className="w-full bg-slate-50 border border-slate-200 text-slate-900 rounded-lg px-4 py-2.5 focus:bg-white focus:ring-2 focus:ring-slate-900 outline-none transition-all text-sm tabular-nums font-bold" placeholder="500" value={newBudget.limit_amount} onChange={(e) => setNewBudget({ ...newBudget, limit_amount: e.target.value })} required />
                    </div>
                    <button type="submit" className="w-full bg-slate-900 text-white rounded-lg px-4 py-3 text-sm font-bold tracking-wide hover:bg-slate-800 transition-colors shadow-sm mt-4">Save Budget</button>
                  </form>
                </div>
              </div>

              <div className="lg:col-span-3">
                <div className="flex items-center justify-between mb-6">
                  <div className="text-lg font-extrabold text-slate-900 tracking-tight">Active Budgets</div>
                  <div className="text-[11px] font-bold text-slate-400 uppercase tracking-widest">{budgets.length} {'monitored'}</div>
                </div>
                {budgets.length === 0 ? (
                  <div className="bg-white rounded-2xl shadow-sm border border-slate-200 p-16 flex flex-col items-center justify-center text-center">
                    <div className="w-16 h-16 rounded-2xl bg-slate-100 flex items-center justify-center mb-6">
                      <BudgetsIcon />
                    </div>
                    <h3 className="text-lg font-extrabold text-slate-900 mb-2">No Budgets Configured</h3>
                    <p className="text-sm text-slate-500 max-w-sm leading-relaxed">Create category spending limits to monitor your outflows and maintain financial discipline.</p>
                  </div>
                ) : (
                  <div className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-6">
                    {budgets.map((b) => {
                      const spent = b.spent_amount || 0;
                      const pct = Math.min(100, (spent / b.limit_amount) * 100);
                      const isOver = pct >= 100;
                      const isWarning = pct >= 80 && !isOver;
                      const remaining = Math.max(0, b.limit_amount - spent);
                      return (
                        <div key={b.id} className="bg-white rounded-2xl shadow-sm border border-slate-200 group hover:shadow-lg hover:-translate-y-0.5 transition-all duration-300 overflow-hidden">
                          <div className={`h-1.5 w-full ${isOver ? 'bg-rose-500' : isWarning ? 'bg-amber-400' : 'bg-emerald-500'}`} />
                          <div className="p-6">
                            <div className="flex justify-between items-start mb-5">
                              <div>
                                <div className="text-lg font-extrabold text-slate-900">{b.category}</div>
                                <div className="text-[11px] text-slate-400 mt-1 font-bold uppercase tracking-widest">
                                  {isOver ? 'Over Budget' : isWarning ? 'Approaching Limit' : 'On Track'}
                                </div>
                              </div>
                              <button onClick={() => deleteBudget(b.id)} className="text-slate-300 hover:text-rose-500 transition-colors opacity-0 group-hover:opacity-100 p-1.5 rounded-lg hover:bg-slate-50">
                                <TrashIcon />
                              </button>
                            </div>
                            <div className="flex items-baseline gap-2 mb-5">
                              <span className="text-3xl font-extrabold text-slate-900 tabular-nums tracking-tight">{'$'}{remaining.toFixed(0)}</span>
                              <span className="text-sm text-slate-400 font-semibold">remaining</span>
                            </div>
                            <div>
                              <div className="flex justify-between items-end mb-2">
                                <span className="text-[10px] font-bold text-slate-400 tabular-nums uppercase tracking-wider">{'$'}{spent.toFixed(0)} / {'$'}{b.limit_amount.toFixed(0)}</span>
                                <span className={`text-sm font-extrabold tabular-nums ${isOver ? 'text-rose-600' : isWarning ? 'text-amber-500' : 'text-emerald-500'}`}>{pct.toFixed(0)}%</span>
                              </div>
                              <div className="w-full bg-slate-100 rounded-full h-2.5 overflow-hidden">
                                <div className={`h-full rounded-full transition-all duration-700 ease-out ${isOver ? 'bg-rose-500' : isWarning ? 'bg-amber-400' : 'bg-emerald-500'}`} style={{ width: `${pct}%` }}></div>
                              </div>
                            </div>
                          </div>
                        </div>
                      );
                    })}
                  </div>
                )}
              </div>
            </div>
          </div>
        )}

        {activeTab === 'goals' && (
          <div className="space-y-8">
            <div className="grid grid-cols-1 lg:grid-cols-4 gap-8">
              <div className="lg:col-span-1">
                <div className="bg-white rounded-2xl shadow-sm border border-slate-200 p-8 sticky top-8">
                  <div className="text-lg font-extrabold text-slate-900 mb-6 tracking-tight">Create Milestone</div>
                  <form onSubmit={addGoal} className="space-y-5">
                    <div>
                      <label className="block text-[11px] font-bold text-slate-500 mb-2 uppercase tracking-widest">Goal Name</label>
                      <input type="text" className="w-full bg-slate-50 border border-slate-200 text-slate-900 rounded-lg px-4 py-2.5 focus:bg-white focus:ring-2 focus:ring-slate-900 outline-none transition-all text-sm font-medium" placeholder="e.g. House Down Payment" value={newGoal.name} onChange={(e) => setNewGoal({ ...newGoal, name: e.target.value })} required />
                    </div>
                    <div>
                      <label className="block text-[11px] font-bold text-slate-500 mb-2 uppercase tracking-widest">Target Amount ($)</label>
                      <input type="number" className="w-full bg-slate-50 border border-slate-200 text-slate-900 rounded-lg px-4 py-2.5 focus:bg-white focus:ring-2 focus:ring-slate-900 outline-none transition-all text-sm tabular-nums font-bold" placeholder="50000" value={newGoal.target_amount} onChange={(e) => setNewGoal({ ...newGoal, target_amount: e.target.value })} required />
                    </div>
                    <div>
                      <label className="block text-[11px] font-bold text-slate-500 mb-2 uppercase tracking-widest">Current Balance ($)</label>
                      <input type="number" className="w-full bg-slate-50 border border-slate-200 text-slate-900 rounded-lg px-4 py-2.5 focus:bg-white focus:ring-2 focus:ring-slate-900 outline-none transition-all text-sm tabular-nums font-bold" placeholder="5000" value={newGoal.current_amount} onChange={(e) => setNewGoal({ ...newGoal, current_amount: e.target.value })} />
                    </div>
                    <div>
                      <label className="block text-[11px] font-bold text-slate-500 mb-2 uppercase tracking-widest">Target Date</label>
                      <input type="date" className="w-full bg-slate-50 border border-slate-200 text-slate-900 rounded-lg px-4 py-2.5 focus:bg-white focus:ring-2 focus:ring-slate-900 outline-none transition-all text-sm font-medium" value={newGoal.target_date} onChange={(e) => setNewGoal({ ...newGoal, target_date: e.target.value })} required />
                    </div>
                    <button type="submit" className="w-full bg-slate-900 text-white rounded-lg px-4 py-3 text-sm font-bold tracking-wide hover:bg-slate-800 transition-colors shadow-sm mt-4">Save Target</button>
                  </form>
                </div>
              </div>

              <div className="lg:col-span-3">
                <div className="flex items-center justify-between mb-6">
                  <div className="text-lg font-extrabold text-slate-900 tracking-tight">Financial Milestones</div>
                  <div className="text-[11px] font-bold text-slate-400 uppercase tracking-widest">{goals.length} {'targets'}</div>
                </div>
                {goals.length === 0 ? (
                  <div className="bg-white rounded-2xl shadow-sm border border-slate-200 p-16 flex flex-col items-center justify-center text-center">
                    <div className="w-16 h-16 rounded-2xl bg-slate-100 flex items-center justify-center mb-6">
                      <GoalsIcon />
                    </div>
                    <h3 className="text-lg font-extrabold text-slate-900 mb-2">No Financial Goals Set</h3>
                    <p className="text-sm text-slate-500 max-w-sm leading-relaxed">Define savings milestones to track your progress toward major financial objectives.</p>
                  </div>
                ) : (
                  <div className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-6">
                    {goals.map((g) => {
                      const pct = Math.min(100, (g.current_amount / g.target_amount) * 100);
                      const remaining = g.target_amount - g.current_amount;
                      const progressColor = pct >= 100 ? 'bg-emerald-500' : pct >= 60 ? 'bg-blue-500' : pct >= 30 ? 'bg-indigo-500' : 'bg-slate-400';
                      return (
                        <div key={g.id} className="bg-white rounded-2xl shadow-sm border border-slate-200 group relative overflow-hidden hover:shadow-lg hover:-translate-y-0.5 transition-all duration-300 flex flex-col">
                          <div className={`h-1.5 w-full ${progressColor}`} />
                          <div className="p-6 flex flex-col flex-1">
                            <div className="flex justify-between items-start mb-4">
                              <div className="flex-1 min-w-0 pr-2">
                                <h3 className="text-lg font-extrabold text-slate-900 truncate">{g.name}</h3>
                                <p className="text-[10px] text-slate-400 font-bold uppercase tracking-widest mt-1">Due {g.target_date}</p>
                              </div>
                              <div className="opacity-0 group-hover:opacity-100 transition-opacity flex gap-1.5 shrink-0">
                                <button onClick={() => {
                                  const amount = prompt('Enter new current balance:', g.current_amount);
                                  if (amount !== null) updateGoalProgress(g.id, amount);
                                }} className="text-slate-400 hover:text-slate-900 transition-colors bg-white rounded-full p-1.5 shadow-sm border border-slate-200">
                                  <EditIcon />
                                </button>
                                <button onClick={() => deleteGoal(g.id)} className="text-slate-400 hover:text-rose-500 transition-colors bg-white rounded-full p-1.5 shadow-sm border border-slate-200">
                                  <TrashIcon />
                                </button>
                              </div>
                            </div>
                            <div className="flex items-center gap-4 mb-5 mt-auto pt-4">
                              <div className="relative w-14 h-14 shrink-0">
                                <svg className="w-14 h-14 -rotate-90" viewBox="0 0 56 56">
                                  <circle cx="28" cy="28" r="24" fill="none" stroke="#E2E8F0" strokeWidth="4" />
                                  <circle cx="28" cy="28" r="24" fill="none" stroke="currentColor" strokeWidth="4" strokeDasharray={`${pct * 1.508} 150.8`} strokeLinecap="round" className={pct >= 100 ? 'text-emerald-500' : pct >= 60 ? 'text-blue-500' : pct >= 30 ? 'text-indigo-500' : 'text-slate-400'} style={{ transition: 'stroke-dasharray 0.8s ease' }} />
                                </svg>
                                <div className="absolute inset-0 flex items-center justify-center">
                                  <span className="text-[11px] font-extrabold text-slate-900 tabular-nums">{pct.toFixed(0)}%</span>
                                </div>
                              </div>
                              <div className="flex-1 min-w-0">
                                <div className="text-2xl font-extrabold text-slate-900 tabular-nums tracking-tight">{'$'}{g.current_amount.toLocaleString()}</div>
                                <div className="text-[11px] text-slate-400 font-semibold tabular-nums mt-0.5">of {'$'}{g.target_amount.toLocaleString()} target</div>
                              </div>
                            </div>
                            <div className="w-full bg-slate-100 rounded-full h-2 overflow-hidden">
                              <div className={`h-full rounded-full transition-all duration-700 ease-out ${progressColor}`} style={{ width: `${pct}%` }}></div>
                            </div>
                          </div>
                        </div>
                      );
                    })}
                  </div>
                )}
              </div>
            </div>
          </div>
        )}

        {activeTab === 'profile' && (
          <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
            <div className="bg-white rounded-2xl shadow-sm border border-slate-200 p-8">
              <div className="text-lg font-extrabold text-slate-900 mb-8 tracking-tight">Risk & Strategy Profile</div>
              <form onSubmit={saveProfile} className="space-y-6">
                <div>
                  <label className="block text-[11px] font-bold text-slate-500 mb-2 uppercase tracking-widest">Annual Baseline Income ($)</label>
                  <input type="number" className="w-full bg-slate-50 border border-slate-200 text-slate-900 rounded-lg px-4 py-3 focus:bg-white focus:ring-2 focus:ring-slate-900 outline-none transition-all text-sm tabular-nums font-bold" value={profile.annual_income} onChange={(e) => setProfile({ ...profile, annual_income: parseFloat(e.target.value) })} required />
                </div>
                <div>
                  <label className="block text-[11px] font-bold text-slate-500 mb-2 uppercase tracking-widest">Risk Tolerance</label>
                  <select className="w-full bg-slate-50 border border-slate-200 text-slate-900 rounded-lg px-4 py-3 focus:bg-white focus:ring-2 focus:ring-slate-900 outline-none transition-all text-sm font-medium" value={profile.risk_tolerance} onChange={(e) => setProfile({ ...profile, risk_tolerance: e.target.value })}>
                    <option value="Low">Low (Capital Preservation)</option>
                    <option value="Medium">Medium (Balanced Growth)</option>
                    <option value="High">High (Aggressive Growth)</option>
                  </select>
                </div>
                <div>
                  <label className="block text-[11px] font-bold text-slate-500 mb-2 uppercase tracking-widest">Investment Experience</label>
                  <select className="w-full bg-slate-50 border border-slate-200 text-slate-900 rounded-lg px-4 py-3 focus:bg-white focus:ring-2 focus:ring-slate-900 outline-none transition-all text-sm font-medium" value={profile.investment_experience} onChange={(e) => setProfile({ ...profile, investment_experience: e.target.value })}>
                    <option value="None">None (Beginner)</option>
                    <option value="Basic">Basic (Equities/Bonds)</option>
                    <option value="Advanced">Advanced (Options, Alts)</option>
                  </select>
                </div>
                <div>
                  <label className="block text-[11px] font-bold text-slate-500 mb-2 uppercase tracking-widest">Age</label>
                  <input type="number" className="w-full bg-slate-50 border border-slate-200 text-slate-900 rounded-lg px-4 py-3 focus:bg-white focus:ring-2 focus:ring-slate-900 outline-none transition-all text-sm tabular-nums font-bold" value={profile.age} onChange={(e) => setProfile({ ...profile, age: parseInt(e.target.value) })} required />
                </div>
                <button type="submit" className="w-full bg-slate-900 text-white rounded-lg px-4 py-3.5 text-sm font-bold tracking-wide hover:bg-slate-800 transition-colors shadow-md mt-6">Save Profile Strategy</button>
              </form>
            </div>
            
            <div className="bg-slate-900 rounded-2xl shadow-floating p-12 flex flex-col justify-center items-center text-center text-white relative overflow-hidden border border-slate-800">
              <div className="absolute top-0 right-0 w-80 h-80 bg-blue-600 rounded-full mix-blend-screen filter blur-[80px] opacity-20 -translate-y-1/2 translate-x-1/2"></div>
              <div className="absolute bottom-0 left-0 w-80 h-80 bg-emerald-600 rounded-full mix-blend-screen filter blur-[80px] opacity-20 translate-y-1/2 -translate-x-1/2"></div>
              
              <div className="bg-slate-800/50 p-4 rounded-2xl mb-8 backdrop-blur-sm border border-slate-700">
                 <span className="text-white"><TrendingUpIcon /></span>
              </div>
              <h3 className="text-3xl font-extrabold tracking-tight mb-4 relative z-10">Institutional Allocation</h3>
              <p className="text-slate-400 text-sm leading-relaxed max-w-sm relative z-10 font-medium">
                Your profile parameters dictate the algorithmic allocation managed by the AuraWealth engine. Models dynamically balance risk vectors based on modern portfolio theory.
              </p>
            </div>
          </div>
        )}
      </main>

      {/* Floating AI Chat Assistant Panel */}
      <div className={`fixed right-0 top-0 h-full w-[400px] bg-white shadow-2xl transform transition-transform duration-300 z-50 flex flex-col ${isChatOpen ? 'translate-x-0' : 'translate-x-full'}`}>
        <div className="p-6 border-b border-slate-100 flex items-center justify-between bg-white">
          <h3 className="font-extrabold text-slate-900 flex items-center gap-3 text-base tracking-tight"><SparklesIcon /> Private Advisor AI</h3>
          <button className="text-slate-400 hover:text-slate-900 transition-colors p-2 rounded-lg hover:bg-slate-50" onClick={() => setIsChatOpen(false)}>
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round"><path d="M18 6 6 18"/><path d="m6 6 12 12"/></svg>
          </button>
        </div>

        <div className="flex-1 overflow-y-auto p-6 space-y-6 bg-slate-50">
          {chatMessages.map((msg, index) => (
            <div key={index} className={`flex ${msg.sender === 'user' ? 'justify-end' : 'justify-start'}`}>
              <div className={`max-w-[85%] px-5 py-3.5 text-sm font-medium leading-relaxed shadow-sm ${msg.sender === 'user' ? 'bg-slate-900 text-white rounded-2xl rounded-br-sm' : 'bg-white text-slate-800 rounded-2xl rounded-bl-sm border border-slate-200'}`}>
                {msg.text}
              </div>
            </div>
          ))}
          {isChatLoading && (
            <div className="flex justify-start">
              <div className="max-w-[85%] rounded-2xl px-5 py-4 text-sm bg-white text-slate-500 rounded-bl-sm border border-slate-200 flex gap-1.5 items-center shadow-sm">
                <span className="w-1.5 h-1.5 bg-slate-400 rounded-full animate-bounce"></span>
                <span className="w-1.5 h-1.5 bg-slate-400 rounded-full animate-bounce" style={{ animationDelay: '0.2s' }}></span>
                <span className="w-1.5 h-1.5 bg-slate-400 rounded-full animate-bounce" style={{ animationDelay: '0.4s' }}></span>
              </div>
            </div>
          )}
        </div>

        <form className="p-5 border-t border-slate-200 bg-white shadow-[0_-4px_6px_-1px_rgba(0,0,0,0.02)]" onSubmit={sendChatMessage}>
          <div className="relative">
            <input
              type="text"
              className="w-full bg-slate-50 border border-slate-200 text-slate-900 rounded-xl pl-5 pr-14 py-4 focus:bg-white focus:ring-2 focus:ring-slate-900 focus:border-slate-900 outline-none transition-all text-sm font-medium shadow-inner"
              placeholder="Query your advisor..."
              value={chatInput}
              onChange={(e) => setChatInput(e.target.value)}
            />
            <button type="submit" className="absolute right-2 top-2 bottom-2 bg-slate-900 text-white rounded-lg w-10 flex items-center justify-center hover:bg-slate-800 transition-colors shadow-sm">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round"><path d="m22 2-7 20-4-9-9-4Z"/><path d="M22 2 11 13"/></svg>
            </button>
          </div>
        </form>
      </div>
      
      {/* Overlay */}
      {isChatOpen && (
        <div className="fixed inset-0 bg-slate-900/40 backdrop-blur-sm z-40 lg:hidden" onClick={() => setIsChatOpen(false)}></div>
      )}
    </div>
  );
}
