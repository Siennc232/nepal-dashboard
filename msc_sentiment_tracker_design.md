# Most Significant Change (MSC) Methodology & Sentiment Tracker Design
## For Nepal Community Wellbeing Dashboard

---

## Overview

The Most Significant Change (MSC) methodology, as highlighted by Ryan, offers a "forensic" approach to evaluation that aligns perfectly with our sentiment analysis work. This document outlines how to integrate MSC with a dynamic sentiment tracking system similar to prediction markets.

---

## What is MSC?

MSC is particularly valuable when:
- No baseline data exists
- Need to understand change attribution
- Want to harvest stakeholders' internal evaluations
- Seeking statistically meaningful patterns from qualitative data

**Core MSC Questions:**
1. "What has been the most significant change in [domain] since [timepoint]?"
2. "What do you attribute this change to?"
3. "Was this change positive or negative?"

---

## Proposed Dashboard Integration

### 1. Sentiment Thermometer Panel

```html
<div class="sentiment-tracker-panel">
    <h3>Community Sentiment Tracker</h3>
    
    <!-- Overall Sentiment Thermometer -->
    <div class="thermometer-container">
        <div class="sentiment-gauge">
            <div class="needle" style="transform: rotate(45deg)">↑</div>
            <div class="scale">
                <span class="negative">-100</span>
                <span class="neutral">0</span>
                <span class="positive">+100</span>
            </div>
        </div>
        <p class="sentiment-score">+67 (Optimistic)</p>
        <p class="trend">↑ +12 from last quarter</p>
    </div>
    
    <!-- Domain-Specific Trackers -->
    <div class="domain-sentiments">
        <div class="domain-item">
            <span>Tourism Impact</span>
            <div class="mini-gauge">
                <div class="bar positive" style="width: 78%"></div>
            </div>
            <span class="change">↑ +15</span>
        </div>
        <div class="domain-item">
            <span>Economic Outlook</span>
            <div class="mini-gauge">
                <div class="bar negative" style="width: 45%"></div>
            </div>
            <span class="change">↓ -8</span>
        </div>
        <!-- More domains... -->
    </div>
</div>
```

### 2. Most Significant Changes Panel

```html
<div class="msc-panel">
    <h3>Most Significant Changes Reported</h3>
    
    <!-- Time Period Selector -->
    <select id="msc-timeframe">
        <option>Last 3 months</option>
        <option>Last 6 months</option>
        <option>Last year</option>
        <option>Since 2022</option>
    </select>
    
    <!-- Changes by Category -->
    <div class="msc-categories">
        <div class="positive-changes">
            <h4>Positive Changes</h4>
            <div class="change-item">
                <div class="impact-score high">High Impact</div>
                <p>"New trekking routes opened, bringing tourists to previously isolated villages"</p>
                <span class="attribution">Attributed to: Infrastructure development (78% agreement)</span>
                <span class="frequency">Mentioned by 45 respondents</span>
            </div>
            <!-- More items... -->
        </div>
        
        <div class="negative-changes">
            <h4>Negative Changes</h4>
            <div class="change-item">
                <div class="impact-score medium">Medium Impact</div>
                <p>"Youth leaving for Kathmandu increased"</p>
                <span class="attribution">Attributed to: Limited local opportunities (65% agreement)</span>
                <span class="frequency">Mentioned by 32 respondents</span>
            </div>
        </div>
    </div>
</div>
```

### 3. Sentiment Timeline (Manifold-style)

```javascript
// Chart configuration for sentiment over time
const sentimentChart = {
    type: 'line',
    data: {
        labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
        datasets: [{
            label: 'Overall Sentiment',
            data: [45, 48, 52, 58, 65, 67],
            borderColor: 'rgb(75, 192, 192)',
            backgroundColor: 'rgba(75, 192, 192, 0.2)',
            tension: 0.4
        }, {
            label: 'Tourism Sentiment',
            data: [60, 65, 70, 72, 75, 78],
            borderColor: 'rgb(54, 162, 235)',
            backgroundColor: 'rgba(54, 162, 235, 0.2)',
            tension: 0.4
        }]
    },
    options: {
        responsive: true,
        plugins: {
            annotation: {
                annotations: {
                    // Mark significant events
                    event1: {
                        type: 'line',
                        xMin: 'Mar',
                        xMax: 'Mar',
                        borderColor: 'rgb(255, 99, 132)',
                        borderWidth: 2,
                        label: {
                            content: 'Road opened',
                            enabled: true
                        }
                    }
                }
            }
        }
    }
};
```

---

## Implementation Strategy

### Phase 1: Modify Survey Questions

Add MSC-specific questions:

```markdown
NEW Q78: "Thinking about the past year, what has been the MOST SIGNIFICANT CHANGE in your community?"
- Category: [Economic / Social / Environmental / Infrastructure / Cultural]
- Description: [Open text]
- Impact: [Very Negative / Negative / Neutral / Positive / Very Positive]

NEW Q79: "What do you believe caused this change?"
[Open text with suggested categories]

NEW Q80: "How confident are you this change will continue?"
[Slider: 0-100%]
```

### Phase 2: Create Sentiment Calculation Engine

```python
def calculate_msc_sentiment(responses_df):
    """
    Calculate sentiment scores from MSC responses
    """
    
    # Weight by impact and confidence
    sentiment_scores = []
    
    for _, row in responses_df.iterrows():
        impact_map = {
            'Very Negative': -100,
            'Negative': -50,
            'Neutral': 0,
            'Positive': 50,
            'Very Positive': 100
        }
        
        impact_score = impact_map.get(row['impact'], 0)
        confidence = row['confidence'] / 100  # 0-1 scale
        
        weighted_score = impact_score * confidence
        sentiment_scores.append({
            'score': weighted_score,
            'category': row['category'],
            'attribution': row['attribution']
        })
    
    return pd.DataFrame(sentiment_scores)
```

### Phase 3: Real-time Tracking System

```python
class SentimentTracker:
    def __init__(self):
        self.baseline = self.establish_baseline()
        self.current = {}
        self.history = []
    
    def update_sentiment(self, new_responses):
        """Update sentiment with new MSC responses"""
        
        # Calculate new sentiment
        new_sentiment = calculate_msc_sentiment(new_responses)
        
        # Compare to baseline
        change = new_sentiment['score'].mean() - self.baseline
        
        # Store with timestamp
        self.history.append({
            'timestamp': datetime.now(),
            'overall_sentiment': new_sentiment['score'].mean(),
            'change_from_baseline': change,
            'top_positive': self.get_top_changes(new_sentiment, 'positive'),
            'top_negative': self.get_top_changes(new_sentiment, 'negative'),
            'confidence_level': new_sentiment['confidence'].mean()
        })
        
        return self.generate_dashboard_update()
```

---

## Visualization Components

### 1. Sentiment Gauge (CSS/JS)

```css
.sentiment-gauge {
    width: 200px;
    height: 100px;
    position: relative;
    background: linear-gradient(to right, #ff4444 0%, #ffff44 50%, #44ff44 100%);
    border-radius: 100px 100px 0 0;
}

.needle {
    position: absolute;
    bottom: 0;
    left: 50%;
    transform-origin: bottom center;
    transition: transform 0.5s ease;
}
```

### 2. Change Attribution Sunburst

```javascript
// D3.js sunburst showing change attribution
const attributionData = {
    name: "Changes",
    children: [
        {
            name: "Economic",
            children: [
                {name: "Tourism Growth", value: 45},
                {name: "Job Creation", value: 30}
            ]
        },
        {
            name: "Infrastructure",
            children: [
                {name: "Road Development", value: 55},
                {name: "Airport Improvement", value: 25}
            ]
        }
    ]
};
```

---

## AI Analysis Prompts for MSC

### Initial Analysis Prompt:
```
"Analyze these Most Significant Change responses:

1. Categorize changes by domain and sentiment
2. Identify causal attributions
3. Calculate confidence-weighted sentiment scores
4. Find patterns in change descriptions
5. Predict future sentiment trajectory

Output format:
- Overall sentiment: [-100 to +100]
- Top 3 positive changes with attribution
- Top 3 negative changes with attribution
- Emerging themes
- Confidence interval for predictions"
```

### Follow-up Investigation Prompt:
```
"The sentiment index shows a sharp decline in [domain]. 
Analyze responses to understand:
1. Root causes of the decline
2. Stakeholder groups most affected
3. Proposed solutions from respondents
4. Timeline of when changes occurred"
```

---

## Benefits of MSC Integration

1. **No Baseline Required**: Perfect for new initiatives
2. **Attribution Clarity**: Understand WHY changes happen
3. **Statistical Validity**: Patterns emerge from stories
4. **Early Warning System**: Sentiment drops trigger investigation
5. **Stakeholder Voice**: Captures internal evaluations
6. **Predictive Power**: Confidence scores indicate future trends

---

## Next Steps

1. Add MSC questions to next survey round
2. Build sentiment calculation engine
3. Create real-time dashboard components
4. Train team on MSC interview techniques
5. Establish regular sentiment tracking cycles

This approach combines the narrative richness of MSC with quantitative tracking, creating a powerful tool for understanding and predicting community wellbeing changes.