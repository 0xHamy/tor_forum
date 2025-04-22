from flask import Flask, render_template

app = Flask(__name__)

# Static data
POSTS = [
    {"id": 1, "title": "Fresh RDP Access - US Servers", "category": "Initial Access", "date": "2025-04-20 14:32", "content": "Selling RDP access to US-based servers. High uptime, clean credentials. DM for pricing.", "poster": "darknet_haxor", "comments": ["Legit seller, vouched!", "How much for 5 servers?"], "type": "seller"},
    {"id": 2, "title": "Corporate VPN Credentials", "category": "Initial Access", "date": "2025-04-19 09:15", "content": "Leaked VPN creds for Fortune 500 company. Access to internal network. $500 BTC.", "poster": "shadow_broker", "comments": ["Interested, sent DM."], "type": "seller"},
    {"id": 3, "title": "AWS Keys - Full Admin", "category": "Initial Access", "date": "2025-04-18 22:47", "content": "Admin AWS keys for sale. Full control over cloud infra. Serious buyers only.", "poster": "cloud_king", "comments": [], "type": "seller"},
    {"id": 4, "title": "SQLi Dump - E-commerce Site", "category": "Data Breach", "date": "2025-04-18 16:20", "content": "Recent SQLi dump from e-commerce site. 10k user records. $200 XMR.", "poster": "data_reaper", "comments": ["Sample data available?"], "type": "seller"},
    {"id": 5, "title": "Windows Exploit Kit", "category": "Exploits", "date": "2025-04-17 11:05", "content": "Custom exploit kit for Windows 10/11. Zero-day included. $1000 BTC.", "poster": "zero_day", "comments": [], "type": "seller"},
    {"id": 6, "title": "Seeking SSH Access", "category": "Buyer Request", "date": "2025-04-17 08:30", "content": "Looking for SSH access to Linux servers. Budget $300. PM me.", "poster": "ghost_user", "comments": ["I have some, DM sent."], "type": "buyer"},
    {"id": 7, "title": "Phishing Template Pack", "category": "Tools", "date": "2025-04-16 19:42", "content": "20+ phishing templates for banking sites. High conversion rate. $150.", "poster": "phish_master", "comments": [], "type": "seller"},
    {"id": 8, "title": "Want RDP for EU Banks", "category": "Buyer Request", "date": "2025-04-16 12:10", "content": "Need RDP access to EU banking servers. Paying $400 BTC. Escrow OK.", "poster": "bank_runner", "comments": [], "type": "buyer"},
    {"id": 9, "title": "Botnet for Hire", "category": "Services", "date": "2025-04-15 23:55", "content": "10k botnet nodes available for DDoS or other tasks. $50/day. Contact me.", "poster": "bot_lord", "comments": ["Reliable service, used before."], "type": "seller"},
    {"id": 10, "title": "Leaked Database - Healthcare", "category": "Data Breach", "date": "2025-04-15 10:25", "content": "Healthcare DB with 50k patient records. $300 XMR. Clean data.", "poster": "med_hack", "comments": [], "type": "seller"}
]

MEMBERS = [
    {"username": "darknet_haxor", "join_date": "2025-04-20"},
    {"username": "shadow_broker", "join_date": "2025-04-19"},
    {"username": "cloud_king", "join_date": "2025-04-18"},
    {"username": "data_reaper", "join_date": "2025-04-17"},
    {"username": "zero_day", "join_date": "2025-04-16"},
    {"username": "ghost_user", "join_date": "2025-04-15"},
    {"username": "phish_master", "join_date": "2025-04-14"},
    {"username": "bank_runner", "join_date": "2025-04-13"},
    {"username": "bot_lord", "join_date": "2025-04-12"},
    {"username": "med_hack", "join_date": "2025-04-11"}
]

@app.route('/')
def index():
    return render_template('index.html', posts=POSTS[:10], members=MEMBERS[:10])

@app.route('/marketplace')
def marketplace():
    return render_template('marketplace.html')

@app.route('/marketplace/buyers')
def buyers():
    buyer_posts = [p for p in POSTS if p['type'] == 'buyer']
    return render_template('buyers.html', posts=buyer_posts)

@app.route('/marketplace/sellers')
def sellers():
    seller_posts = [p for p in POSTS if p['type'] == 'seller']
    return render_template('sellers.html', posts=seller_posts)

@app.route('/post/<int:post_id>')
def post_detail(post_id):
    post = next((p for p in POSTS if p['id'] == post_id), None)
    if not post:
        return "Post not found", 404
    return render_template('post.html', post=post)