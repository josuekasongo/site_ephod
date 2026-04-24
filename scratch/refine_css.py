import re
import os

def refine_css():
    css_path = 'd:\\EPHOD\\css\\style.css'
    with open(css_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Define the new Refined Elite CSS block
    new_banner_css = """
/* ============================================================
   REFINED ELITE IDENTITY (Universal Professional Banner)
   ============================================================ */
.noir-rouge-elite-banner {
  background: radial-gradient(circle at 20% 35%, rgba(140, 19, 56, 0.1) 0%, transparent 70%), 
              radial-gradient(circle at 80% 65%, rgba(140, 19, 56, 0.05) 0%, transparent 60%), 
              #080808 !important;
  color: #ffffff;
  overflow: hidden;
  position: relative;
  min-height: 500px;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 100px 0;
}

.noir-rouge-elite-banner::before {
  content: '';
  position: absolute;
  top: 0; left: 0; right: 0; bottom: 0;
  background: linear-gradient(135deg, rgba(140,19,56,0.02) 0%, transparent 50%, rgba(0,0,0,0.1) 100%);
  pointer-events: none;
}

.noir-rouge-elite-banner .orb-1 { 
  position: absolute; width: 600px; height: 600px; border-radius: 50%; filter: blur(120px);
  background: radial-gradient(circle, rgba(140, 19, 56, 0.08) 0%, transparent 80%); 
  opacity: 0.8; top: -10%; left: -10%;
  animation: orb-drift-slow 30s infinite alternate ease-in-out;
}

.noir-rouge-elite-banner .orb-2 { 
  position: absolute; width: 500px; height: 500px; border-radius: 50%; filter: blur(120px);
  background: radial-gradient(circle, rgba(140, 19, 56, 0.05) 0%, transparent 75%); 
  opacity: 0.6; top: 50%; right: 5%;
  animation: orb-drift-slow 35s infinite alternate-reverse ease-in-out;
}

@keyframes orb-drift-slow {
  0% { transform: translate(0, 0) scale(1); }
  100% { transform: translate(60px, 40px) scale(1.15); }
}

.brand-identity-stack {
  display: inline-flex;
  flex-direction: column;
  align-items: center;
  position: relative;
  margin-bottom: 2rem;
  opacity: 0;
  transform: translateY(30px);
  transition: all 1.2s cubic-bezier(0.2, 1, 0.3, 1);
}

.brand-identity-stack.typing-active {
  opacity: 1;
  transform: translateY(0);
}

.brand-main {
  font-size: clamp(3.5rem, 10vw, 7.5rem);
  font-weight: 950;
  letter-spacing: -3px;
  line-height: 0.9;
  color: #ffffff;
  text-shadow: 0 10px 40px rgba(0,0,0,0.5);
  background: linear-gradient(to bottom, #ffffff 60%, #cccccc 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.brand-sub {
  font-size: clamp(0.9rem, 2vw, 1.4rem);
  font-weight: 300;
  color: var(--accent-red);
  letter-spacing: clamp(10px, 1.5vw, 18px);
  text-transform: uppercase;
  margin-top: 15px;
  opacity: 0.9;
}

.brand-accent-line {
  width: 0%;
  max-width: 600px;
  height: 2px;
  background: linear-gradient(to right, transparent, var(--accent-red), transparent);
  margin-top: 30px;
  transition: width 1.5s ease-out 0.5s;
}

.brand-identity-stack.typing-active .brand-accent-line {
  width: 100%;
}

.institutional-manifesto {
  max-width: 950px;
  margin: 3.5rem auto 0;
  background: rgba(255, 255, 255, 0.03);
  backdrop-filter: blur(25px);
  border: 1px solid rgba(255, 255, 255, 0.08);
  border-left: 5px solid var(--accent-red);
  padding: 3rem 4rem;
  border-radius: 8px;
  text-align: left;
  opacity: 0;
  transform: translateY(20px);
  transition: all 1.5s ease-out 0.8s;
}

.institutional-manifesto.typing-active {
  opacity: 1;
  transform: translateY(0);
}

.institutional-manifesto p {
  color: rgba(255, 255, 255, 0.9);
  font-size: clamp(1rem, 1.3vw, 1.15rem);
  line-height: 2;
  font-weight: 300;
  margin: 0;
  letter-spacing: 0.5px;
}
"""
    # Remove the old messy CSS block (from line 3510 to 3660 roughly)
    # Search for common markers
    start_marker = ".srv-banner-animated.noir-rouge-elite-banner"
    end_marker = ".text-accent-red"
    
    start_idx = content.find(start_marker)
    end_idx = content.find(end_marker)
    
    if start_idx != -1 and end_idx != -1:
        prefix = content[:start_idx]
        suffix = content[end_idx:]
        new_content = prefix + new_banner_css + "\n\n" + suffix
        with open(css_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("CSS Refined successfully.")
    else:
        print("Markers not found.")

if __name__ == "__main__":
    refine_css()
