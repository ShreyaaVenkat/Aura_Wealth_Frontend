import os

def run():
    app_path = "src/App.jsx"
    if not os.path.exists(app_path):
        print(f"Could not find {app_path}")
        return

    with open(app_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    boundary_idx = -1
    for i, line in enumerate(lines):
        if "if (!token) {" in line:
            boundary_idx = i
            break
            
    if boundary_idx == -1:
        print("Boundary not found")
        return

    logic_code = "".join(lines[:boundary_idx])

    new_jsx = """  if (!token) {
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
                  <div className="flex items-end gap-6 h-64 mt-4">
                    {Object.entries(expenseCategories).map(([cat, val]) => (
                      <div className="flex-1 flex flex-col justify-end group" key={cat}>
                        <div
                          className="bg-slate-200 hover:bg-blue-600 transition-all duration-300 rounded-t-lg relative"
                          style={{ height: `${(val / maxCategoryValue) * 100}%`, minHeight: '8px' }}
                        >
                          <div className="opacity-0 group-hover:opacity-100 absolute -top-10 left-1/2 -translate-x-1/2 bg-slate-900 text-white text-xs font-bold py-1.5 px-3 rounded-md whitespace-nowrap transition-opacity shadow-md pointer-events-none">
                            ${val.toFixed(0)}
                          </div>
                        </div>
                        <div className="text-[11px] font-semibold text-slate-500 text-center mt-3 truncate w-full px-1">{cat}</div>
                      </div>
                    ))}
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
          <div className="grid grid-cols-1 xl:grid-cols-3 gap-8">
            <div className="xl:col-span-1">
              <div className="bg-white rounded-2xl shadow-sm border border-slate-200 p-8">
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

            <div className="xl:col-span-2">
              <div className="text-lg font-extrabold text-slate-900 mb-6 tracking-tight">Active Budgets</div>
              {budgets.length === 0 ? (
                <div className="bg-white rounded-2xl shadow-sm border border-slate-200 p-12 flex items-center justify-center text-slate-400 text-sm font-medium">No active budgets defined.</div>
              ) : (
                <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                  {budgets.map((b) => {
                    const spent = b.spent_amount || 0;
                    const pct = Math.min(100, (spent / b.limit_amount) * 100);
                    const isOver = pct >= 100;
                    const isWarning = pct >= 80 && !isOver;
                    return (
                      <div key={b.id} className="bg-white rounded-2xl shadow-sm border border-slate-200 p-6 group hover:shadow-md transition-shadow">
                        <div className="flex justify-between items-start mb-6">
                          <div>
                            <div className="text-base font-extrabold text-slate-900">{b.category}</div>
                            <div className="text-xs text-slate-500 mt-1 tabular-nums font-medium">Remaining: <span className="font-bold">${Math.max(0, b.limit_amount - spent).toFixed(2)}</span></div>
                          </div>
                          <button onClick={() => deleteBudget(b.id)} className="text-slate-300 hover:text-rose-500 transition-colors opacity-0 group-hover:opacity-100 p-1">
                            <TrashIcon />
                          </button>
                        </div>
                        <div>
                           <div className="flex justify-between items-end mb-2">
                             <span className="text-[11px] font-bold text-slate-500 tabular-nums uppercase tracking-wider">${spent.toFixed(2)} / ${b.limit_amount.toFixed(2)}</span>
                             <span className={`text-sm font-extrabold tabular-nums ${isOver ? 'text-rose-600' : isWarning ? 'text-amber-500' : 'text-emerald-500'}`}>{pct.toFixed(0)}%</span>
                           </div>
                           <div className="w-full bg-slate-100 rounded-full h-3 overflow-hidden">
                             <div className={`h-full rounded-full transition-all duration-500 ${isOver ? 'bg-rose-500' : isWarning ? 'bg-amber-400' : 'bg-slate-900'}`} style={{ width: `${pct}%` }}></div>
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

        {activeTab === 'goals' && (
          <div className="grid grid-cols-1 xl:grid-cols-3 gap-8">
            <div className="xl:col-span-1">
              <div className="bg-white rounded-2xl shadow-sm border border-slate-200 p-8">
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

            <div className="xl:col-span-2">
              <div className="text-lg font-extrabold text-slate-900 mb-6 tracking-tight">Financial Milestones</div>
              {goals.length === 0 ? (
                <div className="bg-white rounded-2xl shadow-sm border border-slate-200 p-12 flex items-center justify-center text-slate-400 text-sm font-medium">No financial goals active.</div>
              ) : (
                <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                  {goals.map((g) => {
                    const pct = Math.min(100, (g.current_amount / g.target_amount) * 100);
                    return (
                      <div key={g.id} className="bg-white rounded-2xl shadow-sm border border-slate-200 p-8 flex flex-col justify-between group relative overflow-hidden hover:shadow-md transition-all">
                        <div className="absolute top-0 right-0 p-6 opacity-0 group-hover:opacity-100 transition-opacity flex gap-2">
                          <button onClick={() => {
                            const amount = prompt('Enter new current balance:', g.current_amount);
                            if (amount !== null) updateGoalProgress(g.id, amount);
                          }} className="text-slate-400 hover:text-slate-900 transition-colors bg-white rounded-full p-2 shadow-sm border border-slate-200">
                            <EditIcon />
                          </button>
                          <button onClick={() => deleteGoal(g.id)} className="text-slate-400 hover:text-rose-500 transition-colors bg-white rounded-full p-2 shadow-sm border border-slate-200">
                            <TrashIcon />
                          </button>
                        </div>
                        
                        <div>
                          <h3 className="text-xl font-extrabold text-slate-900 mb-2">{g.name}</h3>
                          <p className="text-[11px] text-slate-500 font-bold uppercase tracking-widest">Target: {g.target_date}</p>
                        </div>
                        <div className="mt-10">
                          <div className="flex justify-between items-end mb-3">
                            <span className="text-base font-extrabold text-slate-900 tabular-nums tracking-tight">${g.current_amount.toLocaleString()} <span className="text-slate-400 text-sm font-semibold">/ ${g.target_amount.toLocaleString()}</span></span>
                            <span className="text-sm font-extrabold text-slate-900">{pct.toFixed(0)}%</span>
                          </div>
                          <div className="w-full bg-slate-100 rounded-full h-3 overflow-hidden">
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
"""

    with open(app_path, "w", encoding="utf-8") as f:
        f.write(logic_code + new_jsx)

    print("Successfully rewrote App.jsx with V2 Premium UI")

if __name__ == "__main__":
    run()
