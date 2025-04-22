from app import db, User, Category, Post, Comment
from datetime import datetime, timedelta
import random
from faker import Faker
from app import app

fake = Faker()

# Helper to generate random dates in Jan-Mar 2025
def random_date():
    start = datetime(2025, 1, 1)
    end = datetime(2025, 3, 31)
    delta = end - start
    random_days = random.randrange(delta.days)
    return start + timedelta(days=random_days)

# Clear existing data
with app.app_context():
    db.drop_all()
    db.create_all()
    print("Database cleared and recreated.")


# Create users
users = [
    {"username": "CyberPhantom", "bio": "Elite hacker specializing in network intrusion.", "reputation": "High"},
    {"username": "ShadowByte", "bio": "Data broker with a knack for leaks.", "reputation": "Trusted"},
    {"username": "ZeroExploit", "bio": "Exploit developer, zero-days for sale.", "reputation": "High"},
    {"username": "DarkViper", "bio": "RDP and VPN access provider.", "reputation": "Trusted"},
    {"username": "GhostRoot", "bio": "Looking for rare access, PM me.", "reputation": "Neutral"},
    {"username": "NeonCracker", "bio": "Phishing expert, custom kits available.", "reputation": "Trusted"},
    {"username": "CrypticWolf", "bio": "Botnet operator, DDoS services.", "reputation": "High"},
    {"username": "StealthNinja", "bio": "Stealthy ops, seeking corporate access.", "reputation": "Neutral"},
    {"username": "DataSpecter", "bio": "Database leaks and dumps.", "reputation": "Trusted"},
    {"username": "QuantumHax", "bio": "General hacking, open to collabs.", "reputation": "Neutral"}
]


with app.app_context():
    for user_data in users:
        user = User(
            username=user_data["username"],
            join_date=random_date(),
            bio=user_data["bio"],
            reputation=user_data["reputation"]
        )
        db.session.add(user)
    db.session.commit()
    print("Created users.")


# Create categories
with app.app_context():
    categories = ["Initial Access", "Help Request", "General", "Account Sales", "Data Leaks"]
    for name in categories:
        category = Category(name=name)
        db.session.add(category)
    db.session.commit()
    print("Created categories.")


# Create posts
posts = [
    {
        "title": "[$6,200] RDP Access - Citibank US Branch Compromised",
        "content": "Yo, got something big. Fresh RDP into Citibank, some branch in New York area, not gonna drop exact deets for OPSEC. This is domain admin level, you basically own their network. Uptime 99.8%, tested for weeks, no flags. Perfect for pulling data, dropping payloads, or whatever you fancy. Price is $6,200 XMR, firm—ain’t no charity here. Can send redacted screenshots or 5-min guest access to prove it’s legit. BTC or XMR, escrow cool if you got rep. PM me quick, this won’t sit long. Serious buyers only, don’t waste my time with lowballs.",
        "type": "seller",
        "category": "Initial Access"
    },
    {
        "title": "[$4,000] VPN Creds - Major Telecom Pwned [EU] - Old Post Removed",
        "content": "Back again, mods nuked my last thread. Selling VPN access to a big EU telecom, one of them household names in Germany (you figure it out). Full internal access, you can pivot to servers, grab call logs, or mess with billing systems. Been stable for a month, no kicks. Asking $4,000 BTC, negotiable for bulk buyers (got 2 more telecoms). I’ll throw in logs or a test connection for proof, but only if you’re serious. Escrow or MM accepted, I’m vouched here. Hit me up in PM, let’s make this quick. No skids, please.",
        "type": "seller",
        "category": "Initial Access"
    },
    {
        "title": "[HOT] $8,500 AWS Keys - Logistics Giant Full Admin - US",
        "content": "Listen up, this is a once-in-a-lifetime drop. Got AWS keys with FULL admin access to a major US logistics corp, think one of those ‘we ship everything’ companies. S3 buckets, EC2 instances, IAM policies—you name it, you control it. Ideal for crypto mining, data dumps, or flipping for profit. Priced at $8,500 XMR, worth every cent. I’m including a bucket list and PoC video for legit buyers, no free rides tho. Payment in XMR only, escrow mandatory for first-timers. Been holding this for the right buyer, so PM me NOW if you got the funds. Don’t sleep on this, it’s a goldmine.",
        "type": "seller",
        "category": "Initial Access"
    },
    {
        "title": "[$3,500] RDP Access - Healthcare Network Hacked - Canada",
        "content": "Hey, i sell RDP to healthcare network in Canada, big hospital group in Ontario, wont say name for safety. This give you admin access to servers, patient data, billing, all that good stuff. Very stable, i check everyday, no problem. Price $3,500 BTC or XMR, can do escrow if you new. I show screenshot or small login to prove it real, but only for real buyer. Good for steal data or ransom, you decide. PM me fast, i got other buyer waiting. No cheap offer, this is premium.",
        "type": "seller",
        "category": "Initial Access"
    },
    {
        "title": "[$5,000] Citrix Access - Retail Chain Pwned - UK - Repost",
        "content": "Alright, reposting since last one got taken down. I got Citrix access to a UK retail chain, one of them big department stores you all shop at (no specifics, keep it OPSEC). Full network admin, you can move lateral, hit their POS systems, or grab customer DBs. Been inside for 2 weeks, rock-solid uptime. Asking $5,000 BTC, XMR also fine. Can provide logs, redacted screenshots, or even a quick tour if you got the coin. Escrow or MM for trust, I’m known here. PM me with your offer, but don’t come with no $500 nonsense. Let’s do business.",
        "type": "seller",
        "category": "General"
    },
    {"title": "Need Help with SQL Injection", "content": "Struggling with SQLi on a target site. Anyone got tips or tools? Willing to pay $50 XMR.", "type": "buyer", "category": "Help Request"},    {"title": "General Discussion: OpSec Tips", "content": "Sharing my OpSec setup: VPN + Tor + burner devices. What's your approach?", "type": "seller", "category": "General"},
    {"title": "Hacked Netflix Accounts", "content": "100+ premium Netflix accounts, $5 each. Bulk discounts available.", "type": "seller", "category": "Account Sales"},
    {"title": "Data Leak - E-commerce DB", "content": "Leaked DB from e-commerce site, 20k user records. $250 XMR.", "type": "seller", "category": "Data Leaks"},
    {"title": "Seeking VPN Access", "content": "Looking for corporate VPN credentials. Budget $400 BTC, escrow OK.", "type": "buyer", "category": "Initial Access"},
    {"title": "Custom Phishing Kit", "content": "20 phishing templates for banks and crypto exchanges. $150 BTC.", "type": "seller", "category": "General"},
    {"title": "Botnet Rental - 15k Nodes", "content": "Rent my botnet for DDoS or scraping. $60/day, BTC only.", "type": "seller", "category": "General"},
    {"title": "Healthcare DB Leak", "content": "50k patient records from hospital DB. Clean data, $350 XMR.", "type": "seller", "category": "Data Leaks"},
    {"title": "Need Exploit for Windows 11", "content": "Seeking zero-day exploit for Win11. Budget $1000 BTC.", "type": "buyer", "category": "Help Request"},
    {"title": "SSN and CC Dump", "content": "Fresh dump, 10k SSNs and CCs. $200 XMR, samples available.", "type": "seller", "category": "Data Leaks"},
    {"title": "General: Best Anonymity Tools?", "content": "What tools do you use for staying anonymous? Tails, Whonix, or other?", "type": "seller", "category": "General"},
    {"title": "Hacked PayPal Accounts", "content": "50 verified PayPal accounts with balance. $10 each, BTC.", "type": "seller", "category": "Account Sales"},
    {"title": "Seeking RDP for EU Servers", "content": "Need RDP access to EU servers, budget $250 BTC.", "type": "buyer", "category": "Initial Access"},
    {"title": "SQLi Tool for Sale", "content": "Custom SQLi tool, bypasses WAF. $100 BTC.", "type": "seller", "category": "General"},
    {"title": "Leaked Employee Credentials", "content": "100+ corporate employee creds, $150 XMR.", "type": "seller", "category": "Data Leaks"},
    {"title": "Help: Bypassing 2FA", "content": "Need advice on bypassing 2FA for a target. $75 XMR for help.", "type": "buyer", "category": "Help Request"},
    {"title": "Crypto Wallet Accounts", "content": "Hacked crypto wallet accounts, $15 each.", "type": "seller", "category": "Account Sales"},
    {"title": "DDoS Service Available", "content": "Professional DDoS service, $100/day. Contact for details.", "type": "seller", "category": "General"},
    {"title": "Seeking AWS Access", "content": "Looking for AWS keys with S3 access. $500 BTC.", "type": "buyer", "category": "Initial Access"},
    {"title": "Bank Login Dump", "content": "5k bank logins, US and EU. $300 XMR.", "type": "seller", "category": "Data Leaks"},
    {"title": "General: Favorite Hacking Tools", "content": "What's your go-to tool? Metasploit, Burp, or custom?", "type": "seller", "category": "General"},
    {"title": "Spotify Premium Accounts", "content": "200 Spotify accounts, $3 each, bulk deals.", "type": "seller", "category": "Account Sales"},
    {"title": "Need Help with Phishing", "content": "Setting up a phishing campaign, need templates. $100 XMR.", "type": "buyer", "category": "Help Request"},
    {"title": "Leaked University DB", "content": "10k student records from US university. $200 XMR.", "type": "seller", "category": "Data Leaks"},
    {"title": "[Royal Bank Canada (RBC)] Limited SMB Access for sale", "content": "I have got limited read/write access to a SMB share of RBC bank Canada, Halton Hills branch. The access is limited so I am selling for $1000, original price was $3000, I will give you a Ubuntu VPS with from where you can access the SMB share. Serious buyers only, LTC & XMR accepted.", "type": "seller", "category": "Initial Access"},
    {"title": "Seeking Botnet Rental", "content": "Need botnet for testing, budget $50/day.", "type": "buyer", "category": "General"},
    {"title": "Custom Malware for Sale", "content": "RAT with advanced features, $500 BTC.", "type": "seller", "category": "General"},
    {"title": "Hacked Social Media Accounts", "content": "100+ Instagram accounts, $8 each.", "type": "seller", "category": "Account Sales"},
    {"title": "General: Crypto Laundering Tips", "content": "How do you launder BTC? Mixers or other methods?", "type": "seller", "category": "General"},
    {"title": "Data Leak - Retail Chain", "content": "20k customer records from retail DB. $250 XMR.", "type": "seller", "category": "Data Leaks"},
    {"title": "Need VPN Creds", "content": "Seeking VPN access for tech company. $300 BTC.", "type": "buyer", "category": "Initial Access"},
    {"title": "Exploit Kit - Browser Based", "content": "Browser exploit kit, works on Chrome/FF. $600 BTC.", "type": "seller", "category": "General"},
    {"title": "Help: Cracking Hashcat", "content": "Need help optimizing Hashcat for MD5. $50 XMR.", "type": "buyer", "category": "Help Request"},
    {"title": "Leaked HR Database", "content": "5k employee records, US company. $150 XMR.", "type": "seller", "category": "Data Leaks"},
    {"title": "Hacked Email Accounts", "content": "500 Gmail/Yahoo accounts, $5 each.", "type": "seller", "category": "Account Sales"},
    {"title": "General: Darknet Market Reviews", "content": "Which markets are legit in 2025? Share experiences.", "type": "seller", "category": "General"},
    {"title": "Seeking DDoS Service", "content": "Need DDoS for a project, budget $100/day.", "type": "buyer", "category": "General"},
    {"title": "Custom Backdoor Tool", "content": "Persistent backdoor for Windows, $400 BTC.", "type": "seller", "category": "General"},
    {"title": "Data Leak - Gaming Platform", "content": "15k user accounts from gaming site. $200 XMR.", "type": "seller", "category": "Data Leaks"},
    {"title": "Need Exploit Advice", "content": "Looking for advice on exploiting old CMS. $75 XMR.", "type": "buyer", "category": "Help Request"}
]



with app.app_context():
    users = User.query.all()
    categories = Category.query.all()
    for post_data in posts:
        post = Post(
            title=post_data["title"],
            content=post_data["content"],
            date=random_date(),
            type=post_data["type"],
            user_id=random.choice(users).id,
            category_id=Category.query.filter_by(name=post_data["category"]).first().id
        )
        db.session.add(post)
    db.session.commit()


comments = [
        "Legit seller, fast delivery!", "Can you provide a sample?", "Interested, sent DM.",
        "Vouched, used before.", "What's the uptime?", "Need more details, PM me.",
        "Great service, reliable.", "Any discounts for bulk?", "Looks good, checking escrow.",
        "Worked perfectly, thanks!", "How recent is the data?", "Can you do custom targets?"
    ]

# Create comments
with app.app_context():
    posts = Post.query.all()
    users = User.query.all()  # Re-query users in the same session
    
    for post in posts:
        num_comments = random.randint(0, 3)
        for _ in range(num_comments):
            comment = Comment(
                content=random.choice(comments),
                date=random_date(),
                user_id=random.choice(users).id,  # Now uses attached users
                post_id=post.id
            )
            db.session.add(comment)
    db.session.commit()
    print("Database populated successfully!")

