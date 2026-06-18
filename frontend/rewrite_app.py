import os

def run():
    app_path = "src/App.jsx"
    if not os.path.exists(app_path):
        print(f"Could not find {app_path}")
        return

    with open(app_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    # Find the boundary: "  // Authentication View" or "if (!token) {"
    boundary_idx = -1
    for i, line in enumerate(lines):
        if "if (!token) {" in line:
            boundary_idx = i
            break
            
    if boundary_idx == -1:
        print("Boundary not found")
        return

    logic_code = "".join(lines[:boundary_idx])

    # The new JSX
    new_jsx = """  if (!token) {
    return (
      <div className="min-h-screen bg-slate-50 flex items-center justify-center p-4 font-sans text-slate-900">
        <div className="bg-white p-8 rounded-2xl shadow-floating max-w-md w-full border border-slate-100">
          <div className="text-center mb-8">
            <span className="inline-block text-slate-900 mb-4">
              <DiamondIcon />
            </span>
            <h2 className="text-2xl font-bold text-slate-900 tracking-tight">AuraWealth</h2>
            <p className="text-slate-500 mt-2 text-sm">
              {isLoginView ? 'Welcome back! Sign in to analyze your assets.' : 'Create an account to start wealth planning.'}
            </p>
          </div>
          <form onSubmit={handleAuth} className="space-y-5">
            <div>
              <label className="block text-sm font-medium text-slate-700 mb-1.5">Email Address</label>
              <input
                type="email"
                className="w-full bg-slate-50 border border-slate-200 text-slate-900 rounded-lg px-4 py-2.5 focus:bg-white focus:ring-2 focus:ring-slate-900 focus:border-slate-900 outline-none transition-all text-sm"
                placeholder="you@example.com"
                value={authEmail}
                onChange={(e) => setAuthEmail(e.target.value)}
                required
              />
            </div>
            <div>
              <label className="block text-sm font-medium text-slate-700 mb-1.5">Password</label>
              <input
                type="password"
                className="w-full bg-slate-50 border border-slate-200 text-slate-900 rounded-lg px-4 py-2.5 focus:bg-white focus:ring-2 focus:ring-slate-900 focus:border-slate-900 outline-none transition-all text-sm"
                placeholder="••••••••"
                value={authPassword}
                onChange={(e) => setAuthPassword(e.target.value)}
                required
              />
            </div>
            <button type="submit" className="w-full bg-slate-900 text-white rounded-lg px-4 py-3 text-sm font-medium hover:bg-slate-800 transition-colors shadow-sm">
              {isLoginView ? 'Sign In' : 'Get Started'}
            </button>
          </form>
          <div className="mt-6 text-center text-sm text-slate-500">
            {isLoginView ? (
              <p>Don't have an account? <span className="text-slate-900 font-medium cursor-pointer hover:underline" onClick={() => setIsLoginView(false)}>Sign Up</span></p>
            ) : (
              <p>Already have an account? <span className="text-slate-900 font-medium cursor-pointer hover:underline" onClick={() => setIsLoginView(true)}>Sign In</span></p>
            )}
          </div>
        </div>
        {toast.message && (
          <div className={`fixed bottom-4 right-4 px-6 py-3 rounded-lg shadow-floating text-sm font-medium text-white ${toast.type === 'error' ? 'bg-rose-500' : 'bg-slate-900'}`}>
            {toast.message}
          </div>
        )}
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-slate-50 flex font-sans text-slate-900 overflow-hidden">
      {/* Sidebar Navigation */}
      <aside className="w-64 bg-white border-r border-slate-200 flex flex-col justify-between h-screen shrink-0 relative z-20">
        <div>
          <div className="p-6 flex items-center gap-3">
            <span className="text-slate-900"><DiamondIcon /></span>
            <span className="font-bold text-lg tracking-tight text-slate-900">AuraWealth</span>
          </div>
          <ul className="px-4 space-y-1">
            <li className={`flex items-center gap-3 px-3 py-2.5 rounded-lg cursor-pointer transition-colors duration-200 ${activeTab === 'dashboard' ? 'bg-slate-100 text-slate-900 font-medium' : 'text-slate-500 hover:bg-slate-50 hover:text-slate-900'}`} onClick={() => setActiveTab('dashboard')}>
              <DashboardIcon /> <span className="text-sm">Dashboard</span>
            </li>
            <li className={`flex items-center gap-3 px-3 py-2.5 rounded-lg cursor-pointer transition-colors duration-200 ${activeTab === 'transactions' ? 'bg-slate-100 text-slate-900 font-medium' : 'text-slate-500 hover:bg-slate-50 hover:text-slate-900'}`} onClick={() => setActiveTab('transactions')}>
              <TransactionsIcon /> <span className="text-sm">Transactions</span>
            </li>
            <li className={`flex items-center gap-3 px-3 py-2.5 rounded-lg cursor-pointer transition-colors duration-200 ${activeTab === 'budgets' ? 'bg-slate-100 text-slate-900 font-medium' : 'text-slate-500 hover:bg-slate-50 hover:text-slate-900'}`} onClick={() => setActiveTab('budgets')}>
              <BudgetsIcon /> <span className="text-sm">Budgets</span>
            </li>
            <li className={`flex items-center gap-3 px-3 py-2.5 rounded-lg cursor-pointer transition-colors duration-200 ${activeTab === 'goals' ? 'bg-slate-100 text-slate-900 font-medium' : 'text-slate-500 hover:bg-slate-50 hover:text-slate-900'}`} onClick={() => setActiveTab('goals')}>
              <GoalsIcon /> <span className="text-sm">Goals</span>
            </li>
            <li className={`flex items-center gap-3 px-3 py-2.5 rounded-lg cursor-pointer transition-colors duration-200 ${activeTab === 'profile' ? 'bg-slate-100 text-slate-900 font-medium' : 'text-slate-500 hover:bg-slate-50 hover:text-slate-900'}`} onClick={() => setActiveTab('profile')}>
              <RiskProfileIcon /> <span className="text-sm">Risk Profile</span>
            </li>
          </ul>
        </div>
        <div className="p-4 m-4 bg-slate-50 rounded-xl border border-slate-100 flex items-center justify-between">
          <div className="flex items-center gap-3 overflow-hidden">
            <div className="w-8 h-8 rounded-full bg-slate-200 text-slate-700 font-bold flex items-center justify-center text-sm shrink-0">{email.charAt(0).toUpperCase()}</div>
            <div className="overflow-hidden">
              <div className="text-xs font-semibold text-slate-900 truncate">{email}</div>
              <div className="text-[10px] text-slate-500 uppercase tracking-wider font-medium mt-0.5">Aura Pro User</div>
            </div>
          </div>
          <button className="text-slate-400 hover:text-rose-600 transition-colors p-1" onClick={handleLogout} title="Sign Out">
            <LogoutIcon />
          </button>
        </div>
      </aside>

      {/* Main View Area */}
      <main className="flex-1 h-screen overflow-y-auto p-8 lg:p-10 scroll-smooth relative z-10">
        <header className="flex flex-col md:flex-row md:items-center justify-between mb-8 gap-4">
          <div>
            <h1 className="text-2xl font-bold text-slate-900 tracking-tight">{activeTab.charAt(0).toUpperCase() + activeTab.slice(1)} Dashboard</h1>
            <p className="text-slate-500 text-sm mt-1">Welcome back, AuraWealth helps you optimize savings velocity.</p>
          </div>
          <div className="flex items-center gap-3">
            <button onClick={compileAdvisory} disabled={isCompiling} className="flex items-center gap-2 px-4 py-2 bg-white border border-slate-200 rounded-lg shadow-sm text-sm font-medium text-slate-700 hover:bg-slate-50 transition-colors disabled:opacity-50">
              <SparklesIcon /> {isCompiling ? 'Analyzing...' : 'Sync AI Advice'}
            </button>
            <button onClick={() => setIsChatOpen(!isChatOpen)} className="flex items-center gap-2 px-4 py-2 bg-slate-900 text-white rounded-lg shadow-sm text-sm font-medium hover:bg-slate-800 transition-colors">
              <ChatIcon /> {isChatOpen ? 'Close Assistant' : 'Ask AI Advisor'}
            </button>
          </div>
        </header>

        {toast.message && (
          <div className={`fixed bottom-4 right-4 px-6 py-3 rounded-lg shadow-floating text-sm font-medium text-white z-50 ${toast.type === 'error' ? 'bg-rose-500' : 'bg-slate-900'}`}>
            {toast.message}
          </div>
        )}

        {activeTab === 'dashboard' && (
          <div className="space-y-6">
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
              <div className="bg-white rounded-xl shadow-card border border-slate-100 p-6 flex flex-col justify-between hover:shadow-md transition-shadow duration-200">
                <div className="text-xs font-semibold text-slate-500 uppercase tracking-wider mb-2">Monthly Inflows</div>
                <div className="text-3xl font-bold text-slate-900 tabular-nums mb-1">${totalIncome.toLocaleString(undefined, { minimumFractionDigits: 2, maximumFractionDigits: 2 })}</div>
                <div className="text-xs font-medium inline-flex items-center px-2 py-0.5 rounded-full w-max bg-emerald-50 text-emerald-600">Active Payroll surplus</div>
              </div>
              <div className="bg-white rounded-xl shadow-card border border-slate-100 p-6 flex flex-col justify-between hover:shadow-md transition-shadow duration-200">
                <div className="text-xs font-semibold text-slate-500 uppercase tracking-wider mb-2">Monthly Spending</div>
                <div className="text-3xl font-bold text-slate-900 tabular-nums mb-1">${totalExpense.toLocaleString(undefined, { minimumFractionDigits: 2, maximumFractionDigits: 2 })}</div>
                <div className="text-xs font-medium inline-flex items-center px-2 py-0.5 rounded-full w-max bg-rose-50 text-rose-600">Capital outflows</div>
              </div>
              <div className="bg-white rounded-xl shadow-card border border-slate-100 p-6 flex flex-col justify-between hover:shadow-md transition-shadow duration-200">
                <div className="text-xs font-semibold text-slate-500 uppercase tracking-wider mb-2">Net Monthly Savings</div>
                <div className="text-3xl font-bold text-slate-900 tabular-nums mb-1">${netSavings.toLocaleString(undefined, { minimumFractionDigits: 2, maximumFractionDigits: 2 })}</div>
                <div className="text-xs font-medium inline-flex items-center px-2 py-0.5 rounded-full w-max bg-emerald-50 text-emerald-600">Surplus margin</div>
              </div>
              <div className="bg-white rounded-xl shadow-card border border-slate-100 p-6 flex flex-col justify-between hover:shadow-md transition-shadow duration-200">
                <div className="text-xs font-semibold text-slate-500 uppercase tracking-wider mb-2">Savings Velocity</div>
                <div className="text-3xl font-bold text-slate-900 tabular-nums mb-1">{savingsRate.toFixed(1)}%</div>
                <div className={`text-xs font-medium inline-flex items-center px-2 py-0.5 rounded-full w-max ${savingsRate >= 20 ? 'bg-emerald-50 text-emerald-600' : 'bg-amber-50 text-amber-600'}`}>
                  Target benchmark: 20%
                </div>
              </div>
            </div>

            <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
              <div className="lg:col-span-2 bg-white rounded-xl shadow-card border border-slate-100 p-6">
                <div className="text-base font-bold text-slate-900 mb-6 tracking-tight">Expense Category Breakdown</div>
                {Object.keys(expenseCategories).length === 0 ? (
                  <div className="flex flex-col items-center justify-center py-12 text-slate-400">
                    <p className="text-sm">No expense transactions recorded.</p>
                  </div>
                ) : (
                  <div className="flex items-end gap-4 h-48 mt-4">
                    {Object.entries(expenseCategories).map(([cat, val]) => (
                      <div className="flex-1 flex flex-col justify-end group" key={cat}>
                        <div
                          className="bg-slate-200 hover:bg-slate-800 transition-all duration-300 rounded-t-md relative"
                          style={{ height: `${(val / maxCategoryValue) * 100}%`, minHeight: '4px' }}
                        >
                          <div className="opacity-0 group-hover:opacity-100 absolute -top-8 left-1/2 -translate-x-1/2 bg-slate-900 text-white text-[10px] py-1 px-2 rounded whitespace-nowrap transition-opacity pointer-events-none">
                            ${val.toFixed(0)}
                          </div>
                        </div>
                        <div className="text-[10px] text-slate-500 text-center mt-2 truncate w-full px-1">{cat}</div>
                      </div>
                    ))}
                  </div>
                )}
              </div>

              <div className="bg-white rounded-xl shadow-card border border-slate-100 p-6 flex flex-col">
                <div className="text-base font-bold text-slate-900 mb-6 tracking-tight">Advisor Status</div>
                <div className="space-y-4 flex-1">
                  <div className="bg-slate-50 p-4 rounded-lg border border-slate-100">
                    <div className="text-[10px] text-slate-500 font-semibold uppercase tracking-wider mb-1">Asset Risk profile</div>
                    <div className="text-lg font-bold text-slate-900">{profile.risk_tolerance} Allocation</div>
                  </div>
                  <div className="bg-slate-50 p-4 rounded-lg border border-slate-100">
                    <div className="text-[10px] text-slate-500 font-semibold uppercase tracking-wider mb-1">Budget Compliance</div>
                    <div className="text-lg font-bold text-emerald-600">
                      {budgets.length > 0 ? `${budgets.length} Categories Monitored` : 'No Active Budgets'}
                    </div>
                  </div>
                </div>
                <button onClick={() => setActiveTab('profile')} className="mt-4 w-full px-4 py-2 bg-white border border-slate-200 rounded-lg shadow-sm text-sm font-medium text-slate-700 hover:bg-slate-50 transition-colors">
                  Update Financial Stats
                </button>
              </div>
            </div>

            <div className="bg-white rounded-xl shadow-card border border-slate-100 p-6">
              <div className="flex items-center justify-between mb-6 border-b border-slate-100 pb-4">
                <div className="flex items-center gap-2">
                  <span className="text-slate-900"><SparklesIcon /></span>
                  <h3 className="text-base font-bold text-slate-900 tracking-tight">Compiled Wealth Advice Report</h3>
                </div>
                <span className="text-xs font-medium text-slate-400">LangGraph Output</span>
              </div>
              {advisorReport ? (
                <div className="prose prose-sm prose-slate max-w-none prose-headings:font-bold prose-a:text-blue-600" dangerouslySetInnerHTML={{ __html: parseMarkdown(advisorReport) }} />
              ) : (
                <div className="text-center py-12">
                  <p className="text-slate-500 text-sm mb-4">No advice compiled. Trigger the AI engine to synthesize your data.</p>
                  <button onClick={compileAdvisory} className="px-4 py-2 bg-slate-900 text-white rounded-lg shadow-sm text-sm font-medium hover:bg-slate-800 transition-colors" disabled={isCompiling}>
                    {isCompiling ? 'Running AI Engine...' : 'Run Analysis'}
                  </button>
                </div>
              )}
            </div>
          </div>
        )}

        {activeTab === 'transactions' && (
          <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
            <div className="lg:col-span-1 space-y-6">
              <div className="bg-white rounded-xl shadow-card border border-slate-100 p-6">
                <div className="text-base font-bold text-slate-900 mb-6 tracking-tight">Add Transaction</div>
                <form onSubmit={addTransaction} className="space-y-4">
                  <div>
                    <label className="block text-xs font-medium text-slate-700 mb-1.5 uppercase tracking-wider">Type</label>
                    <select className="w-full bg-slate-50 border border-slate-200 text-slate-900 rounded-lg px-3 py-2 focus:bg-white focus:ring-2 focus:ring-slate-900 outline-none transition-all text-sm" value={newTx.type} onChange={(e) => setNewTx({ ...newTx, type: e.target.value })}>
                      <option value="expense">Expense (Outflow)</option>
                      <option value="income">Income (Inflow)</option>
                    </select>
                  </div>
                  <div>
                    <label className="block text-xs font-medium text-slate-700 mb-1.5 uppercase tracking-wider">Amount ($)</label>
                    <input type="number" step="0.01" className="w-full bg-slate-50 border border-slate-200 text-slate-900 rounded-lg px-3 py-2 focus:bg-white focus:ring-2 focus:ring-slate-900 outline-none transition-all text-sm tabular-nums" placeholder="0.00" value={newTx.amount} onChange={(e) => setNewTx({ ...newTx, amount: e.target.value })} required />
                  </div>
                  <div>
                    <label className="block text-xs font-medium text-slate-700 mb-1.5 uppercase tracking-wider">Category</label>
                    <select className="w-full bg-slate-50 border border-slate-200 text-slate-900 rounded-lg px-3 py-2 focus:bg-white focus:ring-2 focus:ring-slate-900 outline-none transition-all text-sm" value={newTx.category} onChange={(e) => setNewTx({ ...newTx, category: e.target.value })}>
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
                    <label className="block text-xs font-medium text-slate-700 mb-1.5 uppercase tracking-wider">Date</label>
                    <input type="date" className="w-full bg-slate-50 border border-slate-200 text-slate-900 rounded-lg px-3 py-2 focus:bg-white focus:ring-2 focus:ring-slate-900 outline-none transition-all text-sm" value={newTx.date} onChange={(e) => setNewTx({ ...newTx, date: e.target.value })} required />
                  </div>
                  <div>
                    <label className="block text-xs font-medium text-slate-700 mb-1.5 uppercase tracking-wider">Description</label>
                    <input type="text" className="w-full bg-slate-50 border border-slate-200 text-slate-900 rounded-lg px-3 py-2 focus:bg-white focus:ring-2 focus:ring-slate-900 outline-none transition-all text-sm" placeholder="e.g. Starbucks" value={newTx.description} onChange={(e) => setNewTx({ ...newTx, description: e.target.value })} required />
                  </div>
                  <button type="submit" className="w-full bg-slate-900 text-white rounded-lg px-4 py-2.5 text-sm font-medium hover:bg-slate-800 transition-colors shadow-sm mt-2">Record Transaction</button>
                </form>
              </div>

              <div className="bg-white rounded-xl shadow-card border border-slate-100 p-6">
                <div className="text-sm font-bold text-slate-900 mb-2 tracking-tight">Import CSV</div>
                <p className="text-xs text-slate-500 mb-4 leading-relaxed">Expected columns: amount, category, date, type, description</p>
                <input type="file" accept=".csv" className="hidden" ref={fileInputRef} onChange={handleCSVUpload} />
                <button onClick={() => fileInputRef.current.click()} className="w-full flex items-center justify-center gap-2 px-4 py-2 bg-white border border-slate-200 rounded-lg shadow-sm text-sm font-medium text-slate-700 hover:bg-slate-50 transition-colors">
                  <UploadIcon /> Choose CSV File
                </button>
              </div>
            </div>

            <div className="lg:col-span-2 bg-white rounded-xl shadow-card border border-slate-100 overflow-hidden flex flex-col h-full">
              <div className="p-6 border-b border-slate-100">
                <h3 className="text-base font-bold text-slate-900 tracking-tight">Transaction Log</h3>
              </div>
              <div className="flex-1 overflow-x-auto">
                {transactions.length === 0 ? (
                  <div className="flex items-center justify-center h-48 text-slate-400 text-sm">No transactions recorded.</div>
                ) : (
                  <table className="w-full text-left border-collapse">
                    <thead>
                      <tr className="bg-slate-50 border-b border-slate-100">
                        <th className="px-6 py-3 text-xs font-semibold text-slate-500 uppercase tracking-wider whitespace-nowrap">Date & Desc</th>
                        <th className="px-6 py-3 text-xs font-semibold text-slate-500 uppercase tracking-wider">Category</th>
                        <th className="px-6 py-3 text-xs font-semibold text-slate-500 uppercase tracking-wider text-right">Amount</th>
                        <th className="px-6 py-3"></th>
                      </tr>
                    </thead>
                    <tbody className="divide-y divide-slate-100">
                      {transactions.map((tx) => (
                        <tr key={tx.id} className="hover:bg-slate-50 transition-colors group">
                          <td className="px-6 py-4">
                            <div className="text-sm font-medium text-slate-900">{tx.description}</div>
                            <div className="text-xs text-slate-500 mt-0.5">{tx.date}</div>
                          </td>
                          <td className="px-6 py-4">
                            <span className="px-2.5 py-1 rounded-md text-[11px] font-medium bg-slate-100 text-slate-600 tracking-wide uppercase">{tx.category}</span>
                          </td>
                          <td className={`px-6 py-4 text-right text-sm font-bold tabular-nums ${tx.type === 'expense' ? 'text-slate-900' : 'text-emerald-600'}`}>
                            {tx.type === 'expense' ? '-' : '+'}${tx.amount.toFixed(2)}
                          </td>
                          <td className="px-6 py-4 text-right">
                            <button onClick={() => deleteTransaction(tx.id)} className="text-slate-300 hover:text-rose-600 transition-colors opacity-0 group-hover:opacity-100">
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
          <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
            <div className="lg:col-span-1">
              <div className="bg-white rounded-xl shadow-card border border-slate-100 p-6">
                <div className="text-base font-bold text-slate-900 mb-6 tracking-tight">Set Category Limit</div>
                <form onSubmit={saveBudget} className="space-y-4">
                  <div>
                    <label className="block text-xs font-medium text-slate-700 mb-1.5 uppercase tracking-wider">Category</label>
                    <select className="w-full bg-slate-50 border border-slate-200 text-slate-900 rounded-lg px-3 py-2 focus:bg-white focus:ring-2 focus:ring-slate-900 outline-none transition-all text-sm" value={newBudget.category} onChange={(e) => setNewBudget({ ...newBudget, category: e.target.value })}>
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
                    <label className="block text-xs font-medium text-slate-700 mb-1.5 uppercase tracking-wider">Monthly Limit ($)</label>
                    <input type="number" className="w-full bg-slate-50 border border-slate-200 text-slate-900 rounded-lg px-3 py-2 focus:bg-white focus:ring-2 focus:ring-slate-900 outline-none transition-all text-sm tabular-nums" placeholder="500" value={newBudget.limit_amount} onChange={(e) => setNewBudget({ ...newBudget, limit_amount: e.target.value })} required />
                  </div>
                  <button type="submit" className="w-full bg-slate-900 text-white rounded-lg px-4 py-2.5 text-sm font-medium hover:bg-slate-800 transition-colors shadow-sm mt-2">Define Budget</button>
                </form>
              </div>
            </div>

            <div className="lg:col-span-2 bg-white rounded-xl shadow-card border border-slate-100 p-6">
              <div className="text-base font-bold text-slate-900 mb-6 tracking-tight">Active Budgets</div>
              {budgets.length === 0 ? (
                <div className="flex items-center justify-center h-48 text-slate-400 text-sm">No active budgets defined.</div>
              ) : (
                <div className="space-y-6">
                  {budgets.map((b) => {
                    const spent = b.spent_amount || 0;
                    const pct = Math.min(100, (spent / b.limit_amount) * 100);
                    const isOver = pct >= 100;
                    const isWarning = pct >= 80 && !isOver;
                    return (
                      <div key={b.id} className="group">
                        <div className="flex justify-between items-end mb-2">
                          <div>
                            <div className="text-sm font-bold text-slate-900">{b.category}</div>
                            <div className="text-xs text-slate-500 mt-0.5 tabular-nums">Spent ${spent.toFixed(2)} of ${b.limit_amount.toFixed(2)}</div>
                          </div>
                          <div className="flex items-center gap-3">
                            <span className={`text-xs font-bold tabular-nums ${isOver ? 'text-rose-600' : isWarning ? 'text-amber-500' : 'text-emerald-600'}`}>{pct.toFixed(0)}%</span>
                            <button onClick={() => deleteBudget(b.id)} className="text-slate-300 hover:text-rose-600 transition-colors opacity-0 group-hover:opacity-100">
                              <TrashIcon />
                            </button>
                          </div>
                        </div>
                        <div className="w-full bg-slate-100 rounded-full h-2 overflow-hidden">
                          <div className={`h-full rounded-full transition-all duration-500 ${isOver ? 'bg-rose-500' : isWarning ? 'bg-amber-400' : 'bg-slate-900'}`} style={{ width: `${pct}%` }}></div>
                        </div>
                      </div>
                    );
                  })}
                </div>
              )}
            </div>
          </div>
        )}

        {activeTab === 'goals' && (
          <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
            <div className="lg:col-span-1">
              <div className="bg-white rounded-xl shadow-card border border-slate-100 p-6">
                <div className="text-base font-bold text-slate-900 mb-6 tracking-tight">Create Goal Target</div>
                <form onSubmit={addGoal} className="space-y-4">
                  <div>
                    <label className="block text-xs font-medium text-slate-700 mb-1.5 uppercase tracking-wider">Goal Name</label>
                    <input type="text" className="w-full bg-slate-50 border border-slate-200 text-slate-900 rounded-lg px-3 py-2 focus:bg-white focus:ring-2 focus:ring-slate-900 outline-none transition-all text-sm" placeholder="e.g. House Down Payment" value={newGoal.name} onChange={(e) => setNewGoal({ ...newGoal, name: e.target.value })} required />
                  </div>
                  <div>
                    <label className="block text-xs font-medium text-slate-700 mb-1.5 uppercase tracking-wider">Target Amount ($)</label>
                    <input type="number" className="w-full bg-slate-50 border border-slate-200 text-slate-900 rounded-lg px-3 py-2 focus:bg-white focus:ring-2 focus:ring-slate-900 outline-none transition-all text-sm tabular-nums" placeholder="50000" value={newGoal.target_amount} onChange={(e) => setNewGoal({ ...newGoal, target_amount: e.target.value })} required />
                  </div>
                  <div>
                    <label className="block text-xs font-medium text-slate-700 mb-1.5 uppercase tracking-wider">Current Balance ($)</label>
                    <input type="number" className="w-full bg-slate-50 border border-slate-200 text-slate-900 rounded-lg px-3 py-2 focus:bg-white focus:ring-2 focus:ring-slate-900 outline-none transition-all text-sm tabular-nums" placeholder="5000" value={newGoal.current_amount} onChange={(e) => setNewGoal({ ...newGoal, current_amount: e.target.value })} />
                  </div>
                  <div>
                    <label className="block text-xs font-medium text-slate-700 mb-1.5 uppercase tracking-wider">Target Date</label>
                    <input type="date" className="w-full bg-slate-50 border border-slate-200 text-slate-900 rounded-lg px-3 py-2 focus:bg-white focus:ring-2 focus:ring-slate-900 outline-none transition-all text-sm" value={newGoal.target_date} onChange={(e) => setNewGoal({ ...newGoal, target_date: e.target.value })} required />
                  </div>
                  <button type="submit" className="w-full bg-slate-900 text-white rounded-lg px-4 py-2.5 text-sm font-medium hover:bg-slate-800 transition-colors shadow-sm mt-2">Set Wealth Target</button>
                </form>
              </div>
            </div>

            <div className="lg:col-span-2 bg-white rounded-xl shadow-card border border-slate-100 p-6">
              <div className="text-base font-bold text-slate-900 mb-6 tracking-tight">Goal Tracker</div>
              {goals.length === 0 ? (
                <div className="flex items-center justify-center h-48 text-slate-400 text-sm">No financial goals active.</div>
              ) : (
                <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                  {goals.map((g) => {
                    const pct = Math.min(100, (g.current_amount / g.target_amount) * 100);
                    return (
                      <div key={g.id} className="bg-slate-50 p-5 rounded-xl border border-slate-200 flex flex-col justify-between group relative overflow-hidden">
                        <div className="absolute top-0 right-0 p-4 opacity-0 group-hover:opacity-100 transition-opacity flex gap-2">
                          <button onClick={() => {
                            const amount = prompt('Enter new current balance:', g.current_amount);
                            if (amount !== null) updateGoalProgress(g.id, amount);
                          }} className="text-slate-400 hover:text-slate-900 transition-colors bg-white rounded-full p-1.5 shadow-sm border border-slate-200">
                            <EditIcon />
                          </button>
                          <button onClick={() => deleteGoal(g.id)} className="text-slate-400 hover:text-rose-600 transition-colors bg-white rounded-full p-1.5 shadow-sm border border-slate-200">
                            <TrashIcon />
                          </button>
                        </div>
                        
                        <div>
                          <h3 className="font-bold text-slate-900 mb-1">{g.name}</h3>
                          <p className="text-xs text-slate-500 font-medium">Target: {g.target_date}</p>
                        </div>
                        <div className="mt-6">
                          <div className="flex justify-between items-end mb-2">
                            <span className="text-sm font-semibold text-slate-900 tabular-nums">${g.current_amount.toLocaleString()} <span className="text-slate-400 text-xs font-normal">/ ${g.target_amount.toLocaleString()}</span></span>
                            <span className="text-xs font-bold text-slate-900">{pct.toFixed(0)}%</span>
                          </div>
                          <div className="w-full bg-slate-200 rounded-full h-2 overflow-hidden">
                            <div className="h-full rounded-full bg-slate-900 transition-all duration-500" style={{ width: `${pct}%` }}></div>
                          </div>
                        </div>
                      </div>
                    );
                  })}
                </div>
              )}
            </div>
          </div>
        )}

        {activeTab === 'profile' && (
          <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
            <div className="bg-white rounded-xl shadow-card border border-slate-100 p-6">
              <div className="text-base font-bold text-slate-900 mb-6 tracking-tight">Asset Risk & Financial Profile</div>
              <form onSubmit={saveProfile} className="space-y-5">
                <div>
                  <label className="block text-xs font-medium text-slate-700 mb-1.5 uppercase tracking-wider">Annual Baseline Income ($)</label>
                  <input type="number" className="w-full bg-slate-50 border border-slate-200 text-slate-900 rounded-lg px-4 py-2.5 focus:bg-white focus:ring-2 focus:ring-slate-900 outline-none transition-all text-sm tabular-nums" value={profile.annual_income} onChange={(e) => setProfile({ ...profile, annual_income: parseFloat(e.target.value) })} required />
                </div>
                <div>
                  <label className="block text-xs font-medium text-slate-700 mb-1.5 uppercase tracking-wider">Risk Tolerance</label>
                  <select className="w-full bg-slate-50 border border-slate-200 text-slate-900 rounded-lg px-4 py-2.5 focus:bg-white focus:ring-2 focus:ring-slate-900 outline-none transition-all text-sm" value={profile.risk_tolerance} onChange={(e) => setProfile({ ...profile, risk_tolerance: e.target.value })}>
                    <option value="Low">Low (Safety First, Capital Preservation)</option>
                    <option value="Medium">Medium (Balanced Equity / Bonds Growth)</option>
                    <option value="High">High (Growth Indexing, Crypto, Alternates)</option>
                  </select>
                </div>
                <div>
                  <label className="block text-xs font-medium text-slate-700 mb-1.5 uppercase tracking-wider">Investment Experience Level</label>
                  <select className="w-full bg-slate-50 border border-slate-200 text-slate-900 rounded-lg px-4 py-2.5 focus:bg-white focus:ring-2 focus:ring-slate-900 outline-none transition-all text-sm" value={profile.investment_experience} onChange={(e) => setProfile({ ...profile, investment_experience: e.target.value })}>
                    <option value="None">None (Beginner)</option>
                    <option value="Basic">Basic (Familiar with stocks/ETFs)</option>
                    <option value="Advanced">Advanced (Options, Real Estate, Complex Portfolios)</option>
                  </select>
                </div>
                <div>
                  <label className="block text-xs font-medium text-slate-700 mb-1.5 uppercase tracking-wider">Age</label>
                  <input type="number" className="w-full bg-slate-50 border border-slate-200 text-slate-900 rounded-lg px-4 py-2.5 focus:bg-white focus:ring-2 focus:ring-slate-900 outline-none transition-all text-sm tabular-nums" value={profile.age} onChange={(e) => setProfile({ ...profile, age: parseInt(e.target.value) })} required />
                </div>
                <button type="submit" className="w-full bg-slate-900 text-white rounded-lg px-4 py-3 text-sm font-medium hover:bg-slate-800 transition-colors shadow-sm mt-4">Update Risk Statistics</button>
              </form>
            </div>
            
            <div className="bg-slate-900 rounded-xl shadow-floating p-10 flex flex-col justify-center items-center text-center text-white relative overflow-hidden">
              <div className="absolute top-0 right-0 w-64 h-64 bg-blue-500 rounded-full mix-blend-multiply filter blur-3xl opacity-20 -translate-y-1/2 translate-x-1/2"></div>
              <div className="absolute bottom-0 left-0 w-64 h-64 bg-purple-500 rounded-full mix-blend-multiply filter blur-3xl opacity-20 translate-y-1/2 -translate-x-1/2"></div>
              
              <span className="text-white mb-6 relative z-10"><TrendingUpIcon /></span>
              <h3 className="text-2xl font-bold tracking-tight mb-4 relative z-10">Personalized Allocation</h3>
              <p className="text-slate-300 text-sm leading-relaxed max-w-sm relative z-10">
                Your risk profile metrics feed directly into our intelligent LangGraph investment engine. It automatically adjusts your equity-to-bond ratio depending on age and risk choice to build optimal portfolios.
              </p>
            </div>
          </div>
        )}
      </main>

      {/* Floating AI Chat Assistant Panel */}
      <div className={`fixed right-0 top-0 h-full w-96 bg-white border-l border-slate-200 shadow-2xl transform transition-transform duration-300 z-50 flex flex-col ${isChatOpen ? 'translate-x-0' : 'translate-x-full'}`}>
        <div className="p-5 border-b border-slate-100 flex items-center justify-between bg-slate-50">
          <h3 className="font-bold text-slate-900 flex items-center gap-2 text-sm"><SparklesIcon /> Aura Wealth Advisor</h3>
          <button className="text-slate-400 hover:text-slate-900 transition-colors p-1" onClick={() => setIsChatOpen(false)}>
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="M18 6 6 18"/><path d="m6 6 12 12"/></svg>
          </button>
        </div>

        <div className="flex-1 overflow-y-auto p-5 space-y-4 bg-white">
          {chatMessages.map((msg, index) => (
            <div key={index} className={`flex ${msg.sender === 'user' ? 'justify-end' : 'justify-start'}`}>
              <div className={`max-w-[85%] rounded-2xl px-4 py-2.5 text-sm ${msg.sender === 'user' ? 'bg-slate-900 text-white rounded-br-sm' : 'bg-slate-100 text-slate-800 rounded-bl-sm border border-slate-200'}`}>
                {msg.text}
              </div>
            </div>
          ))}
          {isChatLoading && (
            <div className="flex justify-start">
              <div className="max-w-[85%] rounded-2xl px-4 py-2.5 text-sm bg-slate-100 text-slate-500 rounded-bl-sm border border-slate-200 flex gap-1 items-center">
                <span className="w-1.5 h-1.5 bg-slate-400 rounded-full animate-bounce"></span>
                <span className="w-1.5 h-1.5 bg-slate-400 rounded-full animate-bounce" style={{ animationDelay: '0.2s' }}></span>
                <span className="w-1.5 h-1.5 bg-slate-400 rounded-full animate-bounce" style={{ animationDelay: '0.4s' }}></span>
              </div>
            </div>
          )}
        </div>

        <form className="p-4 border-t border-slate-100 bg-white" onSubmit={sendChatMessage}>
          <div className="relative">
            <input
              type="text"
              className="w-full bg-slate-50 border border-slate-200 text-slate-900 rounded-full pl-4 pr-12 py-3 focus:bg-white focus:ring-2 focus:ring-slate-900 focus:border-slate-900 outline-none transition-all text-sm shadow-sm"
              placeholder="Ask your advisor..."
              value={chatInput}
              onChange={(e) => setChatInput(e.target.value)}
            />
            <button type="submit" className="absolute right-1.5 top-1.5 bottom-1.5 bg-slate-900 text-white rounded-full w-9 flex items-center justify-center hover:bg-slate-800 transition-colors shadow-sm">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round"><path d="m22 2-7 20-4-9-9-4Z"/><path d="M22 2 11 13"/></svg>
            </button>
          </div>
        </form>
      </div>
      
      {/* Overlay for chat drawer on mobile */}
      {isChatOpen && (
        <div className="fixed inset-0 bg-slate-900/20 backdrop-blur-sm z-40 lg:hidden" onClick={() => setIsChatOpen(false)}></div>
      )}
    </div>
  );
}
"""

    with open("src/App.jsx", "w", encoding="utf-8") as f:
        f.write(logic_code + new_jsx)

    print("Successfully rewrote App.jsx")

if __name__ == "__main__":
    run()
