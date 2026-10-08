import os

base_dir = r"C:\Users\Neha\OneDrive\Desktop\SIH\SIH WINNERS\admin-dashboard\src"
os.makedirs(os.path.join(base_dir, "components"), exist_ok=True)
os.makedirs(os.path.join(base_dir, "pages"), exist_ok=True)

files = {
    "App.tsx": """
import React, { useState } from 'react';
import { LayoutDashboard, Users, AlertTriangle, Settings, LogOut } from 'lucide-react';
import DashboardOverview from './pages/DashboardOverview';
import WorkerVerification from './pages/WorkerVerification';

function App() {
  const [activeTab, setActiveTab] = useState('overview');

  return (
    <div className="flex h-screen bg-[#F7F9F8] text-[#26332E]">
      {/* Sidebar */}
      <div className="w-64 bg-white border-r border-[#DDE5E1] flex flex-col">
        <div className="p-6">
          <h1 className="text-2xl font-bold text-[#356B59] tracking-wider">SAHAYA</h1>
          <p className="text-xs text-gray-500 mt-1">Admin Portal</p>
        </div>
        
        <nav className="flex-1 px-4 space-y-2 mt-4">
          <button 
            onClick={() => setActiveTab('overview')}
            className={`w-full flex items-center space-x-3 px-4 py-3 rounded-lg transition-colors ${activeTab === 'overview' ? 'bg-[#356B59] text-white' : 'hover:bg-gray-50'}`}
          >
            <LayoutDashboard size={20} />
            <span className="font-medium">Overview</span>
          </button>
          
          <button 
            onClick={() => setActiveTab('verification')}
            className={`w-full flex items-center space-x-3 px-4 py-3 rounded-lg transition-colors ${activeTab === 'verification' ? 'bg-[#356B59] text-white' : 'hover:bg-gray-50'}`}
          >
            <Users size={20} />
            <span className="font-medium">Verification Queue</span>
          </button>
          
          <button 
            className="w-full flex items-center space-x-3 px-4 py-3 rounded-lg hover:bg-gray-50"
          >
            <AlertTriangle size={20} />
            <span className="font-medium">Disputes</span>
          </button>
        </nav>
        
        <div className="p-4 border-t border-[#DDE5E1]">
          <button className="w-full flex items-center space-x-3 px-4 py-3 rounded-lg hover:bg-gray-50 text-red-600">
            <LogOut size={20} />
            <span className="font-medium">Logout</span>
          </button>
        </div>
      </div>

      {/* Main Content */}
      <div className="flex-1 overflow-auto">
        {activeTab === 'overview' && <DashboardOverview />}
        {activeTab === 'verification' && <WorkerVerification />}
      </div>
    </div>
  )
}

export default App;
""",
    "pages/DashboardOverview.tsx": """
import React from 'react';
import { Activity, TrendingUp, AlertOctagon } from 'lucide-react';

export default function DashboardOverview() {
  return (
    <div className="p-8">
      <h2 className="text-2xl font-bold mb-6 text-[#26332E]">System Overview</h2>
      
      {/* Stats Row */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
        <div className="bg-white p-6 rounded-xl shadow-sm border border-[#DDE5E1]">
          <div className="flex items-center justify-between mb-4">
            <h3 className="text-gray-500 font-medium">Total Workers</h3>
            <Activity className="text-[#4F806B]" />
          </div>
          <p className="text-4xl font-bold text-[#356B59]">2,450</p>
          <p className="text-sm text-green-600 mt-2 flex items-center">
            <TrendingUp size={16} className="mr-1" /> +12% from last month
          </p>
        </div>
        
        <div className="bg-white p-6 rounded-xl shadow-sm border border-[#DDE5E1]">
          <div className="flex items-center justify-between mb-4">
            <h3 className="text-gray-500 font-medium">Pending Verification</h3>
            <Users className="text-[#B38A4A]" />
          </div>
          <p className="text-4xl font-bold text-[#B38A4A]">42</p>
          <p className="text-sm text-gray-500 mt-2">Requires manual review</p>
        </div>
        
        <div className="bg-white p-6 rounded-xl shadow-sm border border-[#DDE5E1]">
          <div className="flex items-center justify-between mb-4">
            <h3 className="text-gray-500 font-medium">Emergency Requests (24h)</h3>
            <AlertOctagon className="text-[#B85C5C]" />
          </div>
          <p className="text-4xl font-bold text-[#B85C5C]">7</p>
          <p className="text-sm text-gray-500 mt-2">All resolved</p>
        </div>
      </div>

      {/* AI Forecast Section */}
      <div className="bg-white rounded-xl shadow-sm border border-[#DDE5E1] p-6 mb-8">
        <h3 className="text-lg font-bold mb-4">AI Demand Forecast (Next 24h)</h3>
        <div className="overflow-x-auto">
          <table className="w-full text-left">
            <thead>
              <tr className="border-b border-[#DDE5E1]">
                <th className="pb-3 text-gray-500 font-medium">Zone</th>
                <th className="pb-3 text-gray-500 font-medium">Service</th>
                <th className="pb-3 text-gray-500 font-medium">Predicted Demand</th>
                <th className="pb-3 text-gray-500 font-medium">Available Workers</th>
                <th className="pb-3 text-gray-500 font-medium">AI Action</th>
              </tr>
            </thead>
            <tbody>
              <tr className="border-b border-[#DDE5E1] last:border-0">
                <td className="py-4 font-medium">Peelamedu</td>
                <td className="py-4">Plumbing</td>
                <td className="py-4 text-[#B85C5C] font-bold">High (↑ 45%)</td>
                <td className="py-4">3</td>
                <td className="py-4"><span className="bg-[#B38A4A]/20 text-[#B38A4A] px-3 py-1 rounded-full text-sm font-medium">Allocate 2 more</span></td>
              </tr>
              <tr>
                <td className="py-4 font-medium">RS Puram</td>
                <td className="py-4">Electrical</td>
                <td className="py-4 text-green-600 font-bold">Normal</td>
                <td className="py-4">8</td>
                <td className="py-4"><span className="bg-green-100 text-green-700 px-3 py-1 rounded-full text-sm font-medium">Optimal</span></td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  )
}
""",
    "pages/WorkerVerification.tsx": """
import React from 'react';
import { CheckCircle, XCircle, FileText } from 'lucide-react';

export default function WorkerVerification() {
  return (
    <div className="p-8">
      <div className="flex justify-between items-center mb-6">
        <h2 className="text-2xl font-bold text-[#26332E]">Worker Verification Queue</h2>
        <span className="bg-[#B38A4A]/20 text-[#B38A4A] px-4 py-2 rounded-full font-bold">
          42 Pending
        </span>
      </div>
      
      <div className="bg-white rounded-xl shadow-sm border border-[#DDE5E1] overflow-hidden">
        <table className="w-full text-left">
          <thead className="bg-gray-50">
            <tr>
              <th className="py-4 px-6 text-gray-500 font-medium">Worker Name</th>
              <th className="py-4 px-6 text-gray-500 font-medium">Cooperative ID</th>
              <th className="py-4 px-6 text-gray-500 font-medium">Primary Skill</th>
              <th className="py-4 px-6 text-gray-500 font-medium">Documents</th>
              <th className="py-4 px-6 text-gray-500 font-medium">Actions</th>
            </tr>
          </thead>
          <tbody className="divide-y divide-[#DDE5E1]">
            <tr className="hover:bg-gray-50">
              <td className="py-4 px-6 font-medium">Anand Kumar</td>
              <td className="py-4 px-6 font-mono text-sm">COOP-TN-8842</td>
              <td className="py-4 px-6">Plumbing</td>
              <td className="py-4 px-6">
                <button className="flex items-center text-blue-600 hover:underline">
                  <FileText size={16} className="mr-1" /> View Aadhaar & Card
                </button>
              </td>
              <td className="py-4 px-6 flex space-x-3">
                <button className="flex items-center text-green-600 hover:bg-green-50 px-3 py-1 rounded border border-green-200">
                  <CheckCircle size={16} className="mr-1" /> Approve
                </button>
                <button className="flex items-center text-red-600 hover:bg-red-50 px-3 py-1 rounded border border-red-200">
                  <XCircle size={16} className="mr-1" /> Reject
                </button>
              </td>
            </tr>
            <tr className="hover:bg-gray-50">
              <td className="py-4 px-6 font-medium">Meena S.</td>
              <td className="py-4 px-6 font-mono text-sm">COOP-TN-9911</td>
              <td className="py-4 px-6">Caregiving</td>
              <td className="py-4 px-6">
                <button className="flex items-center text-blue-600 hover:underline">
                  <FileText size={16} className="mr-1" /> View Aadhaar & Card
                </button>
              </td>
              <td className="py-4 px-6 flex space-x-3">
                <button className="flex items-center text-green-600 hover:bg-green-50 px-3 py-1 rounded border border-green-200">
                  <CheckCircle size={16} className="mr-1" /> Approve
                </button>
                <button className="flex items-center text-red-600 hover:bg-red-50 px-3 py-1 rounded border border-red-200">
                  <XCircle size={16} className="mr-1" /> Reject
                </button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  )
}
"""
}

for path, content in files.items():
    with open(os.path.join(base_dir, path), "w", encoding="utf-8") as f:
        f.write(content.strip())

print("React UI implemented.")
