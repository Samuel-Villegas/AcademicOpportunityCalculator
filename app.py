from flask import Flask, render_template, request

app = Flask(__name__)

# Pre-defined weight assignments (from our script)
weight_assignments = {
    'Housing': {'Owns Property':1, 'Renting':0, 'Homeless':-1},
    'Current Wealth': {'Rich':1, 'Middle Class':0, 'Poor':-1},
    'Language': {'English':1, 'Learned English':0, 'Non-English monolingual':-1},
    'Citizenship': {'Citizen':1,'Documented':0,'Undocumented':-1},
    'Religion & Culture': {'Widely Accepted':1,'Mostly Accepted':0,'Not Widely Accepted':-1},
    'Formal Education': {'Degree(s)':1,'Limited':0,'None':-1},
    'Institution': {'Research Intensive':1,'Equal Teaching & Research':0,'Teaching Intensive':-1},
    'Funding/Resources': {'High':1,'Medium':0,'None / Very Low':-1},
    'Career Stage': {'Late Career':1,'Mid Career':0,'Early Career':-1},
    'Mental Health': {'Robust':1,'Mostly Stable':0,'Vulnerable':-1},
    'Neuro-diversity': {'Neuro-typical':1,'Some Neuro-divergence':0,'Multiply Neuro-divergent':-1},
    'Body size': {'Slim':1,'Average':0,'Large':-1},
    '(Dis)ability': {'Able-bodied':1,'Some Disability':0,'Multiply Disabled':-1},
    'Childhood Household Wealth': {'Rich':1,'Middle Class':0,'Poor':-1},
    'Childhood Household Stability': {'Stable':1,'Mostly Stable':0,'Unstable':-1},
    'Care-Giver Educational Level': {'Tertiary':1,'Secondary':0,'Primary':-1},
    'Caring Duties': {'No Care':1,'Shared Care':0,'Self Care':-1},
    'Gender': {'Cis-man':1,'Cis-woman':0,'Trans, Intersex, Non-binary':-1},
    'Sexuality': {'Hetero-sexual':1,'Gay man':0,'Lesbian, Bi, Pan, Asexual':-1},
    'Skin Colour': {'White':1,'Various Shades':0,'Dark':-1},
}

# Function to calculate privilege score
def calculate_privilege(input_data):
    total_score = 0
    max_score = len(weight_assignments) * 1  # Adjust according to max possible weight
    for category, answer in input_data.items():
        total_score += weight_assignments.get(category, {}).get(answer, 0)
    privilege_percentage = (total_score / max_score) * 100
    return privilege_percentage

# Flask routes
@app.route('/')
def form():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit_form():
    user_input = {}
    for category in weight_assignments:
        user_input[category] = request.form.get(category)
    
    # Calculate the privilege score
    privilege_percentage = calculate_privilege(user_input)
    
    return f'Your privilege score is: {privilege_percentage:.2f}'

if __name__ == '__main__':
    app.run(debug=True)

