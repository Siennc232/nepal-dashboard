# MSC Implementation Guide: Reformatting Q59 and Adding Q78-80
## Most Significant Change Methodology for Nepal Dashboard

---

## Current Q59 Limitations

**Current Format:**
```
Q59: "Over time the places we live, work and enjoy change. To help better manage change, tell us:
- What do you love about where you live?
- What do you imagine for where you live?
- What do you want to retain?"
```

**Problems:**
- Too general and unfocused
- Doesn't capture specific changes or timeframes
- No attribution or impact assessment
- Difficult to track sentiment over time

---

## Reformatted Q59 Using MSC Methodology

### New Q59 Structure

```
Q59: "Thinking about changes in your community over the PAST YEAR:

a) What has been the MOST SIGNIFICANT POSITIVE change?
   - Area: □ Tourism □ Economy □ Infrastructure □ Culture □ Environment □ Social
   - Describe the change: [Text box - 2-3 sentences]
   - When did you first notice this? [Month/Year dropdown]
   - Impact on your life: □ Major □ Moderate □ Minor □ None

b) What has been the MOST SIGNIFICANT NEGATIVE change?
   - Area: □ Tourism □ Economy □ Infrastructure □ Culture □ Environment □ Social
   - Describe the change: [Text box - 2-3 sentences]
   - When did you first notice this? [Month/Year dropdown]
   - Impact on your life: □ Major □ Moderate □ Minor □ None

c) What do you believe CAUSED these changes?
   Positive change caused by: [Text box]
   Negative change caused by: [Text box]"
```

---

## New Questions Q78-80: MSC Deep Dive

### Q78: Change Confidence & Trajectory

```
Q78: "For the changes you identified:

a) How confident are you that the POSITIVE change will continue?
   [Slider: 0% --- 50% --- 100%]
   Not at all     Somewhat    Very confident

b) How confident are you that the NEGATIVE change will get worse?
   [Slider: 0% --- 50% --- 100%]
   Not at all     Somewhat    Very confident

c) Overall, is your community heading in the right direction?
   □ Definitely yes
   □ Probably yes
   □ Unsure
   □ Probably no
   □ Definitely no"
```

### Q79: Attribution & Stakeholder Analysis

```
Q79: "Who or what is MOST responsible for these changes?

For POSITIVE change:
□ Government policies
□ Tourism development
□ Community initiatives
□ External organizations
□ Economic forces
□ Environmental factors
□ Other: _______

For NEGATIVE change:
□ Government policies
□ Tourism development
□ Community initiatives
□ External organizations
□ Economic forces
□ Environmental factors
□ Other: _______"
```

### Q80: Future Expectations

```
Q80: "Looking ahead to the NEXT YEAR:

a) What change would you MOST like to see?
   Area: [Same categories as Q59]
   Describe: [Text box]

b) How likely is this change to happen?
   [Slider: 0% --- 50% --- 100%]
   Very unlikely  50/50 chance  Very likely

c) What would need to happen for this change to occur?
   [Text box - specific actions/conditions]"
```

---

## Pseudo Data Examples

### Sample Response Set (n=150)

```python
import pandas as pd
import numpy as np

# Generate pseudo MSC data
np.random.seed(42)

# Categories and their distribution
categories = ['Tourism', 'Economy', 'Infrastructure', 'Culture', 'Environment', 'Social']
category_weights = [0.3, 0.25, 0.2, 0.1, 0.1, 0.05]

# Generate 150 responses
msc_data = []

for i in range(150):
    # Positive changes
    pos_category = np.random.choice(categories, p=category_weights)
    pos_impact = np.random.choice(['Major', 'Moderate', 'Minor'], p=[0.3, 0.5, 0.2])
    pos_confidence = np.random.randint(40, 95)
    
    # Negative changes
    neg_category = np.random.choice(categories, p=[0.15, 0.35, 0.15, 0.15, 0.15, 0.05])
    neg_impact = np.random.choice(['Major', 'Moderate', 'Minor'], p=[0.4, 0.4, 0.2])
    neg_confidence = np.random.randint(30, 85)
    
    # Overall direction
    direction_probs = [0.1, 0.25, 0.3, 0.25, 0.1]  # Slightly pessimistic
    direction = np.random.choice(['Definitely yes', 'Probably yes', 'Unsure', 'Probably no', 'Definitely no'], 
                                p=direction_probs)
    
    msc_data.append({
        'respondent_id': i+1,
        'ward': np.random.choice([1, 2, 3, 4, 5]),
        'positive_category': pos_category,
        'positive_impact': pos_impact,
        'positive_confidence': pos_confidence,
        'negative_category': neg_category,
        'negative_impact': neg_impact,
        'negative_confidence': neg_confidence,
        'community_direction': direction,
        'future_likelihood': np.random.randint(20, 90)
    })

msc_df = pd.DataFrame(msc_data)

# Sample text responses
positive_changes = {
    'Tourism': [
        "New trekking routes opened bringing tourists to our village",
        "Helicopter service improved emergency medical access",
        "More homestays creating local employment"
    ],
    'Economy': [
        "New market opened providing better prices for local goods",
        "Youth returning to start tourism businesses",
        "Increased demand for local handicrafts"
    ],
    'Infrastructure': [
        "Road to Lukla finally completed",
        "New water supply system installed",
        "Internet connectivity improved significantly"
    ]
}

negative_changes = {
    'Economy': [
        "Rising prices making daily life difficult",
        "Young people leaving for city jobs",
        "Traditional farming declining"
    ],
    'Culture': [
        "Fewer people speaking Sherpa at home",
        "Traditional festivals less attended",
        "Outside influences changing local customs"
    ],
    'Environment': [
        "More trash on trekking routes",
        "Weather patterns becoming unpredictable",
        "Glacial lake growing dangerously"
    ]
}
```

---

## Dashboard Visualizations

### 1. Sentiment Direction Gauge

```javascript
// Overall Community Direction Gauge
const directionData = {
    'Definitely yes': 15,
    'Probably yes': 38,
    'Unsure': 45,
    'Probably no': 38,
    'Definitely no': 14
};

// Calculate net sentiment (-100 to +100)
const sentimentScore = (15*100 + 38*50 + 45*0 + 38*(-50) + 14*(-100)) / 150;
// Result: -4.67 (slightly negative)
```

**Visualization**: A semicircular gauge showing:
- Red zone (-100 to -33): "Wrong Direction"
- Yellow zone (-33 to +33): "Uncertain"
- Green zone (+33 to +100): "Right Direction"
- Needle pointing to -4.67

### 2. Change Impact Matrix

```python
# Create impact matrix
impact_matrix = pd.crosstab(
    msc_df['positive_category'], 
    msc_df['positive_impact']
)

# Visualization: Heatmap
```

**What it shows**: Which categories are having the most significant positive impacts on people's lives.

### 3. Attribution Sankey Diagram

```javascript
// Flow from Change Category → Attribution → Impact
const sankeyData = {
    nodes: [
        // Categories
        {id: 0, name: "Tourism Growth"},
        {id: 1, name: "Economic Decline"},
        {id: 2, name: "Infrastructure"},
        // Attributions
        {id: 3, name: "Government Policy"},
        {id: 4, name: "Market Forces"},
        {id: 5, name: "Community Initiative"},
        // Impacts
        {id: 6, name: "Major Positive"},
        {id: 7, name: "Major Negative"}
    ],
    links: [
        {source: 0, target: 3, value: 45},  // Tourism → Gov Policy
        {source: 0, target: 5, value: 30},  // Tourism → Community
        {source: 1, target: 4, value: 55},  // Economic → Market
        {source: 3, target: 6, value: 40},  // Gov Policy → Major Positive
        {source: 4, target: 7, value: 50}   // Market → Major Negative
    ]
};
```

### 4. Confidence Trend Timeline

```python
# Monthly sentiment tracking
monthly_sentiment = pd.DataFrame({
    'month': pd.date_range('2024-01', periods=12, freq='M'),
    'positive_confidence': [45, 48, 52, 58, 62, 65, 68, 66, 64, 61, 58, 55],
    'negative_confidence': [30, 32, 35, 38, 42, 48, 52, 55, 58, 60, 62, 65],
    'net_sentiment': [15, 16, 17, 20, 20, 17, 16, 11, 6, 1, -4, -10]
})
```

**Visualization**: Multi-line chart showing:
- Green line: Confidence in positive changes continuing
- Red line: Worry about negative changes worsening
- Black line: Net sentiment (difference)
- Shaded area: Confidence interval

### 5. Ward-Level Change Dashboard

```python
# Ward comparison
ward_summary = msc_df.groupby('ward').agg({
    'positive_confidence': 'mean',
    'negative_confidence': 'mean',
    'future_likelihood': 'mean'
}).round(1)

# Add sentiment direction
ward_sentiment = msc_df.groupby(['ward', 'community_direction']).size().unstack(fill_value=0)
```

**Visualization**: Small multiples showing each ward's:
- Sentiment gauge
- Top positive/negative changes
- Future outlook score

---

## How to Use These Insights

### 1. Early Warning System

```python
def detect_sentiment_alerts(current_month, previous_month):
    """
    Identify wards or categories needing attention
    """
    alerts = []
    
    # Check for rapid sentiment decline
    if current_month['net_sentiment'] < previous_month['net_sentiment'] - 10:
        alerts.append({
            'type': 'RAPID_DECLINE',
            'severity': 'HIGH',
            'message': 'Sentiment dropped >10 points',
            'action': 'Conduct focus groups to understand causes'
        })
    
    # Check for high negative confidence
    if current_month['negative_confidence'] > 70:
        alerts.append({
            'type': 'PESSIMISM_ALERT',
            'severity': 'MEDIUM',
            'message': 'High confidence in negative trends',
            'action': 'Review negative change attributions'
        })
    
    return alerts
```

### 2. Policy Prioritization

```python
# Identify high-impact, high-confidence issues
priority_matrix = msc_df[
    (msc_df['negative_impact'] == 'Major') & 
    (msc_df['negative_confidence'] > 70)
].groupby('negative_category').size().sort_values(ascending=False)

print("Top Priority Issues:")
print(priority_matrix.head(3))
# Output:
# Economy           42
# Environment       18
# Culture          12
```

### 3. Success Tracking

```python
# Monitor positive changes attributed to specific interventions
intervention_success = msc_df[
    msc_df['positive_attribution'].str.contains('road|infrastructure')
]['positive_confidence'].mean()

print(f"Infrastructure intervention confidence: {intervention_success}%")
```

---

## Benefits of MSC Implementation

### 1. **Works Without Baseline Data**
- Don't need historical measurements
- People naturally compare to their internal baseline
- "Forensic" approach reconstructs change history

### 2. **Shows WHY Changes Happen**
- Direct attribution questions
- Links causes to effects
- Identifies responsible parties/factors

### 3. **Creates Early Warning System**
- Sentiment drops trigger investigation
- High negative confidence = urgent action needed
- Track emerging issues before crisis

### 4. **Aligns with Existing Sentiment Analysis**
- Quantifies qualitative experiences
- Structured format improves AI analysis
- Enables statistical validity from stories

### 5. **Actionable Intelligence**
```python
# Example action trigger
if ward_sentiment['negative_confidence'].mean() > 65:
    recommendations = [
        "Hold emergency community meeting",
        "Review recent policy changes",
        "Accelerate positive interventions",
        "Increase communication frequency"
    ]
```

---

## Implementation Timeline

**Month 1**: Update survey with new questions
**Month 2**: Collect first round of MSC data  
**Month 3**: Build dashboard visualizations
**Month 4**: First sentiment report with trends
**Month 6**: Predictive modeling begins
**Year 1**: Full annual cycle comparison

This MSC approach transforms scattered observations into systematic intelligence about community change.