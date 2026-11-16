# Dictionary of clean, minimalist SVG icons (1.5px stroke, modern Livspace/editorial style)
ICONS = {
    'kitchen': '''<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M3 11h18v8a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-8z"/><path d="M4 11V7a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v4"/><path d="M9 16h6"/><circle cx="7.5" cy="8" r="1"/><circle cx="16.5" cy="8" r="1"/></svg>''',
    
    'wardrobe': '''<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="18" height="18" rx="2"/><path d="M12 3v18"/><circle cx="9" cy="12" r="1"/><circle cx="15" cy="12" r="1"/></svg>''',
    
    'home': '''<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/></svg>''',
    
    'paneling': '''<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="18" height="18" rx="2"/><line x1="7.5" y1="3" x2="7.5" y2="21"/><line x1="12" y1="3" x2="12" y2="21"/><line x1="16.5" y1="3" x2="16.5" y2="21"/></svg>''',
    
    'ceiling': '''<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><line x1="2" y1="4" x2="22" y2="4"/><path d="M7 4v4a5 5 0 0 0 10 0V4"/><line x1="12" y1="13" x2="12" y2="17"/><path d="M12 21a2 2 0 0 0 2-2h-4a2 2 0 0 0 2 2z"/></svg>''',
    
    'door': '''<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M18 20V6a2 2 0 0 0-2-2H8a2 2 0 0 0-2 2v14"/><path d="M2 20h20"/><circle cx="14" cy="12" r="1"/></svg>''',
    
    'furniture': '''<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M4 18v3"/><path d="M20 18v3"/><path d="M19 11v7H5v-7"/><path d="M19 11a3 3 0 0 0-3-3H8a3 3 0 0 0-3 3"/><path d="M3 14h18"/></svg>''',
    
    'paint': '''<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M18.37 2.63L14 7l3 3 4.37-4.37a2.12 2.12 0 1 0-3-3z"/><path d="M14 7l-9 9v4h4l9-9"/></svg>''',
    
    'mep': '''<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg>'''
}

if __name__ == '__main__':
    print('Icons ready:', len(ICONS))
