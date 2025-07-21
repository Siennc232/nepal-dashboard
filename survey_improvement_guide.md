# Survey Question Improvement Guide for AI Analysis
## Nepal Happiness Index Questionnaire Review

---

## Table of Contents
1. [Executive Summary](#executive-summary)
2. [Formatting Issues](#formatting-issues)
3. [Wellbeing Measurement Limitations](#wellbeing-measurement-limitations)
4. [Open-Ended Question Analysis](#open-ended-question-analysis)
5. [AI Analysis Optimization Principles](#ai-analysis-optimization-principles)
6. [Improved Question Designs](#improved-question-designs)
7. [Prompt Engineering Strategies](#prompt-engineering-strategies)
8. [Implementation Recommendations](#implementation-recommendations)

---

## Executive Summary

This guide analyzes the Nepal Happiness Index survey to identify improvements for better AI analysis and more comprehensive wellbeing measurement. Key findings include formatting inconsistencies, limited future-oriented questions, and open-ended questions that are too broad for effective sentiment analysis.

---

## Formatting Issues

### 1. Inconsistent Scale Presentations

**Current Issues:**
- Q1: Uses 0-10 ladder scale
- Q2-5: Uses text descriptions without clear numeric mapping
- Q41: Reverses scale direction (Overwhelming stress → No stress)

**Impact on AI Analysis:**
- Difficult to standardize responses
- Confusion in reverse-scored items
- Inconsistent data types complicate analysis

**Recommendations:**
```
Standardized Format:
"On a scale of 0-10, where 0 = [negative anchor] and 10 = [positive anchor]"

Example:
Q2: Overall, how satisfied are you with your life nowadays?
0 = Completely dissatisfied
10 = Completely satisfied
[Slider: 0-10]
```

### 2. Language Mixing

**Current Issue:**
Some questions mix English and Nepali inconsistently, making text analysis difficult.

**Solution:**
- Separate language versions completely
- Use consistent terminology
- Provide clear translation keys for AI analysis

### 3. Question Numbering

**Problem:**
Q59 has three sub-parts but they're not clearly numbered, causing data collection issues.

**Fix:**
```
59a. What do you love about where you live?
59b. What do you imagine for where you live?
59c. What do you want to retain?
```

---

## Wellbeing Measurement Limitations

### 1. Missing Future Orientation

**Current Gap:**
- Only Q8 asks about optimism
- No questions about goals, plans, or aspirations

**Add Questions:**
```
NEW: "What are your top 3 goals for the next 5 years?"
NEW: "What would most improve your quality of life?"
NEW: "What skills would you like to develop?"
```

### 2. Limited Behavioral Indicators

**Current Issue:**
Mostly asks about feelings, not actions

**Improvement:**
```
Instead of: "How satisfied are you with community?"
Add: "In the past month, how many times did you:
- Attend community meetings
- Help a neighbor
- Participate in local decisions"
```

### 3. Missing Resilience Measures

**Add Questions:**
```
"When facing difficulties, I can usually find solutions"
"I have people I can rely on in emergencies"
"Our community works together to solve problems"
```

---

## Open-Ended Question Analysis

### Current Open-Ended Questions Review

#### Q57SA: Tourism Comments
**Issues:**
- Too broad and unfocused
- No guidance on what aspects to comment on
- Difficult for AI to categorize responses

**Improved Version:**
```
"Regarding tourism in your area, please comment on:
a) ONE positive impact you've observed
b) ONE negative impact you've experienced
c) ONE specific suggestion for improvement"
```

#### Q59: What do you love about where you live?
**Issues:**
- Too general, leads to vague responses
- Hard to extract actionable insights
- Difficult to compare across respondents

**Improved Structure:**
```
"What do you most value about living here? Choose up to 3:
□ Natural environment
□ Community relationships
□ Cultural traditions
□ Economic opportunities
□ Safety and security
□ Other: [specify]

For each selection, explain why in 1-2 sentences:"
```

#### Q77SA: In one word, what makes you happy?
**Issues:**
- Single word limits analysis depth
- No context for interpretation
- Difficult to identify patterns

**Better Approach:**
```
"Complete this sentence: 'I feel happiest when...'
(Please provide 2-3 specific examples)"
```

---

## AI Analysis Optimization Principles

### 1. Structure for Categorization

**Principle**: Guide responses into analyzable categories while allowing flexibility

**Example Implementation:**
```python
# Poor question for AI analysis
"What are your thoughts on development?"

# Optimized for AI
"Regarding development in your area:
1. Type: □ Economic □ Infrastructure □ Social □ Environmental
2. Impact: □ Very Positive □ Positive □ Neutral □ Negative □ Very Negative
3. Explain your choice (2-3 sentences):"
```

### 2. Balance Structure with Openness

**Key Elements:**
- Provide frameworks without limiting expression
- Use prompts that elicit specific types of information
- Include both categorical and narrative elements

### 3. Enable Sentiment Granularity

**Instead of binary positive/negative:**
```
"Describe your experience with [topic]:
- What worked well?
- What challenges did you face?
- What would you change?"
```

---

## Improved Question Designs

### 1. Enhanced Tourism Impact Assessment

**Original**: "Would you like to make any comments about tourism in your site?"

**Improved Multi-Part Version**:
```
Tourism Impact Assessment:

A. Economic Impact
"How has tourism affected your household income?"
□ Significant increase □ Some increase □ No change □ Some decrease □ Significant decrease
"Explain briefly:"

B. Cultural Impact
"How has tourism affected local traditions?"
□ Strengthened them □ No impact □ Weakened them
"Give one example:"

C. Environmental Impact
"Rate tourism's environmental impact:"
□ Very positive □ Positive □ Neutral □ Negative □ Very negative
"Describe one specific impact you've observed:"

D. Future Vision
"In 10 words or less, describe your ideal tourism future:"
```

### 2. Community Threats Assessment

**Original**: Multiple choice only

**Enhanced Version**:
```
"Rank these threats from 1 (most serious) to 8 (least serious):
___ Climate change
___ Outmigration
___ Cultural loss
___ Economic inequality
___ Land ownership changes
___ Infrastructure strain
___ Environmental degradation
___ Other: ________

For your #1 threat, explain:
a) Why is this most serious? (2-3 sentences)
b) What specific impacts have you observed?
c) What solution would you propose?"
```

### 3. Wellbeing Drivers

**New Question Design**:
```
"Think about a recent time when you felt particularly satisfied with life.
1. When was this? (month/year)
2. What was happening? (2-3 sentences)
3. Which life areas were involved? (check all)
   □ Family □ Work □ Community □ Health □ Culture □ Nature □ Other

This helps AI identify:
- Temporal patterns
- Wellbeing triggers
- Domain interactions"
```

---

## Prompt Engineering Strategies

### 1. For Sentiment Analysis

**Basic Prompt** (Less Effective):
```
"Analyze the sentiment of these tourism comments"
```

**Optimized Prompt**:
```
"Analyze tourism feedback from a Nepal mountain community with this framework:

1. Overall Sentiment Score (-5 to +5)
2. Primary Concerns (list top 3)
3. Positive Aspects Mentioned
4. Specific Issues by Category:
   - Economic
   - Cultural
   - Environmental
   - Infrastructure
5. Actionable Suggestions Extracted
6. Emotional Tone (frustrated/hopeful/resigned/enthusiastic)

For each comment, also note:
- Stakeholder perspective (resident/business owner/youth/elder)
- Time orientation (past/present/future focused)
- Solution orientation (problem-focused vs solution-focused)"
```

### 2. For Pattern Recognition

**Structured Analysis Prompt**:
```
"Identify patterns in 'what makes you happy' responses:

1. Categorize into themes:
   - Relationships (family, friends, community)
   - Activities (work, hobbies, traditions)
   - Environment (nature, place, home)
   - Achievement (goals, progress, contribution)
   - Basic needs (health, food, shelter)

2. For each category:
   - Count frequency
   - Note demographic patterns
   - Identify unique cultural elements

3. Create happiness formula:
   'In this community, happiness = [top 3 factors] + [cultural specifics]'"
```

### 3. For Comparative Analysis

**Temporal Comparison Prompt**:
```
"Compare 2022 vs 2025 responses on community threats:

Analysis Framework:
1. Threat Evolution
   - New threats emerged
   - Threats that intensified
   - Threats that diminished

2. Language Analysis
   - Urgency indicators (words like 'crisis', 'immediate')
   - Hope indicators ('improving', 'managing')
   - Action words vs passive descriptions

3. Solution Sophistication
   - 2022: Problem identification focus?
   - 2025: Solution proposal focus?

4. Community Cohesion Indicators
   - 'We' vs 'They' language
   - Collective vs individual concerns"
```

---

## Implementation Recommendations

### 1. Hybrid Question Format

**Structure**:
```
Part A: Structured Response (for quantification)
Part B: Open Elaboration (for context)
Part C: Specific Example (for validation)
```

**Example - Life Satisfaction**:
```
A. Rate your overall life satisfaction: [0-10 scale]
B. What most contributes to this rating? (2-3 factors)
C. Describe a specific recent experience that reflects this rating:
```

### 2. Progressive Disclosure

Start broad, then narrow:
```
Level 1: "How do you feel about tourism?" [Positive/Neutral/Negative]
Level 2: "Which aspects?" [Economic/Cultural/Environmental/Social]
Level 3: "Specific example?" [Open text with prompts]
```

### 3. Context Anchoring

**Before**: "Are you satisfied with government?"

**After**: 
```
"Thinking about the past year:
- One government action that helped your community:
- One government action that created challenges:
- Your satisfaction level: [0-10]"
```

### 4. Response Templates

Provide fill-in-the-blank structures:
```
"The biggest change I've seen is _______ which has made life _______ because _______"

This helps AI:
- Extract key information consistently
- Compare responses easily
- Identify patterns quickly
```

---

## AI Analysis Code Examples

### 1. Enhanced Sentiment Analysis

```python
def analyze_structured_responses(df):
    """
    Analyzes responses with structured format
    """
    
    # For tourism impact question
    tourism_categories = {
        'economic': ['income', 'job', 'business', 'money'],
        'cultural': ['tradition', 'culture', 'festival', 'language'],
        'environmental': ['nature', 'pollution', 'waste', 'forest'],
        'social': ['community', 'youth', 'family', 'migration']
    }
    
    # Structured prompt for AI
    prompt_template = """
    Analyze this tourism response:
    Economic Impact: {economic_response}
    Cultural Impact: {cultural_response}
    Environmental Impact: {environmental_response}
    Future Vision: {vision_response}
    
    Extract:
    1. Primary concern category
    2. Sentiment by category (-5 to +5)
    3. Specific issues mentioned
    4. Proposed solutions
    5. Overall outlook (optimistic/pessimistic/balanced)
    """
    
    return analyzed_results
```

### 2. Pattern Detection

```python
def detect_wellbeing_patterns(responses):
    """
    Identifies patterns in wellbeing drivers
    """
    
    pattern_prompt = """
    Group these wellbeing experiences by:
    
    1. Temporal patterns:
       - Seasonal (festival, harvest, tourism season)
       - Life events (marriage, birth, achievement)
       - Daily routines (work satisfaction, family time)
    
    2. Social patterns:
       - Individual achievements
       - Family milestones  
       - Community celebrations
    
    3. Domain interactions:
       - Single domain (just work, just family)
       - Multiple domains (work + family + health)
    
    Return pattern strength scores and examples.
    """
```

---

## Quality Assurance Checklist

### For Each Question:
- [ ] Clear, specific language
- [ ] Appropriate response format for AI analysis
- [ ] Balance between structure and openness
- [ ] Cultural sensitivity maintained
- [ ] Temporal anchor when needed
- [ ] Examples or prompts provided
- [ ] Logical flow to next question

### For Open-Ended Questions:
- [ ] Specific enough to guide responses
- [ ] Open enough for authentic expression
- [ ] Structured for easy categorization
- [ ] Includes context anchors
- [ ] Requests specific examples
- [ ] Appropriate length limits

### For AI Analysis:
- [ ] Responses can be categorized
- [ ] Sentiment can be extracted
- [ ] Patterns can be identified
- [ ] Comparisons are possible
- [ ] Actionable insights can be derived

---

## Conclusion

By implementing these improvements, the survey will generate data that is:
1. More analyzable by AI tools
2. Richer in actionable insights
3. Better at capturing wellbeing complexity
4. Easier to track over time
5. More useful for policy decisions

The key is balancing structure with authenticity - guiding responses enough for analysis while preserving the genuine voice of respondents.