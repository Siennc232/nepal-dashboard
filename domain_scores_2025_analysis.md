# Nepal Dashboard - Domain Scores Analysis for 2025

## Summary of Calculated Domain Scores

Based on analysis of the Nepal-Grid view.csv file containing 560 survey responses, here are the calculated domain scores for 2025:

### Domain Scores (Calculated from Raw Data)

1. **Domain 1: Satisfaction with Life & Affect** - 63.3%
   - Based on Q1-Q5 (2,649 valid responses)
   - Measures life satisfaction, happiness, anxiety levels

2. **Domain 2: Psychological Well-being** - 78.7%
   - Based on Q6-Q10 (2,784 valid responses)
   - Measures purpose, engagement, optimism, accomplishment

3. **Domain 3: Health** - 67.1%
   - Based on Q11-Q14 (2,232 valid responses)
   - Measures self-rated health, energy, daily activities, exercise

4. **Domain 4: Time Balance** - 58.9%
   - Based on Q15-Q17 (1,672 valid responses)
   - Measures time for enjoyment, feeling rushed, spare time

5. **Domain 5: Community** - 54.5%
   - Based on Q18-Q24 (3,903 valid responses)
   - Measures belonging, trust, safety, volunteering

6. **Domain 6: Social Support** - 63.1%
   - Based on Q25-Q28 (2,216 valid responses)
   - Measures relationships, feeling cared for, loved, lonely

7. **Domain 7: Lifelong Learning, Arts & Culture** - 54.8%
   - Based on Q29-Q32 (2,210 valid responses)
   - Measures access to sports, arts, education, cultural inclusion

8. **Domain 8: Environment** - 73.4%
   - Based on Q33-Q36 (2,209 valid responses)
   - Measures physical environment health, nature access, air quality

9. **Domain 9: Government** - 50.8%
   - Based on Q37-Q40 (2,212 valid responses)
   - Measures corruption perception, government responsiveness, trust

10. **Domain 10: Standard of Living / Economy** - 37.8%
    - Based on Q41-Q44 (2,205 valid responses)
    - Measures financial stress, living paycheck to paycheck, food security

11. **Domain 11: Work** - 68.2%
    - Based on Q45-Q50 (3,249 valid responses)
    - Measures work satisfaction, work-life balance, productivity

12. **Domain 12: Tourism** - 70.3%
    - Based on Q51-Q56 (2,648 valid responses; note Q52 excluded as it's not a score)
    - Measures tourism satisfaction, local benefits, sustainability

### Overall Average: 61.7%

## Comparison with Dashboard Display

The dashboard (nepal-dashboard-updated v3.html) shows the following scores:

| Domain | Dashboard Score | Calculated Score | Difference |
|--------|----------------|------------------|------------|
| Life Satisfaction | 66% | 63.3% | -2.7% |
| Psychological Wellbeing | 78% | 78.7% | +0.7% |
| Health | 67% | 67.1% | +0.1% |
| Time Balance | 59% | 58.9% | -0.1% |
| Community | 55% | 54.5% | -0.5% |
| Social Support | 71% | 63.1% | -7.9% |
| Lifelong Learning & Culture | 65% | 54.8% | -10.2% |
| Environment | 74% | 73.4% | -0.6% |
| Government | 58% | 50.8% | -7.2% |
| Economy | 53% | 37.8% | -15.2% |
| Tourism | 72% | 70.3% | -1.7% |
| **Overall Average** | **66%** | **61.7%** | **-4.3%** |

## Key Discrepancies

1. **Economy Domain**: The dashboard shows 53%, but the calculated score is 37.8% - a significant 15.2% difference. This is the largest discrepancy.

2. **Lifelong Learning & Culture**: Dashboard shows 65%, calculated is 54.8% - a 10.2% difference.

3. **Social Support**: Dashboard shows 71%, calculated is 63.1% - a 7.9% difference.

4. **Government**: Dashboard shows 58%, calculated is 50.8% - a 7.2% difference.

5. **Overall Average**: Dashboard shows 66%, calculated is 61.7% - a 4.3% difference.

## Notes on Calculation Method

- Scores were calculated by converting all response percentages to numeric values
- Domain scores are the average of all valid responses for questions within that domain
- The overall average is the mean of all 12 domain scores
- Some respondents did not answer all questions, resulting in varying numbers of valid responses per domain

## CSV File Pre-calculated Averages

The CSV file contains some pre-calculated domain averages in specific columns. These generally align more closely with the dashboard values than our raw calculations, suggesting the dashboard may be using these pre-calculated values rather than computing from raw scores.