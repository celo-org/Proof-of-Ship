#!/usr/bin/env python3
import os
import re
import glob

def extract_scores_from_file(filepath):
    """Extract Mento scores from an analysis markdown file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract repository name from filename
        filename = os.path.basename(filepath)
        repo_name = filename.replace('-analysis.md', '').replace('-', '/')
        
        scores = {}
        
        # Look for the project scores table
        score_patterns = {
            'mento_sdk': r'Mento SDK Integration Quality.*?(\d+\.?\d*)/10',
            'broker': r'Broker Contract Usage.*?(\d+\.?\d*)/10',
            'oracle': r'Oracle Implementation.*?(\d+\.?\d*)/10',
            'swap': r'Swap Functionality.*?(\d+\.?\d*)/10',
            'code_quality': r'Code Quality & Architecture.*?(\d+\.?\d*)/10',
            'overall': r'Overall Technical Score.*?(\d+\.?\d*)/10'
        }
        
        for category, pattern in score_patterns.items():
            match = re.search(pattern, content, re.IGNORECASE | re.DOTALL)
            if match:
                scores[category] = float(match.group(1))
            else:
                scores[category] = 0.0
        
        return repo_name, scores
        
    except Exception as e:
        print(f"Error processing {filepath}: {e}")
        return None, None

def main():
    # Get all analysis files
    analysis_files = glob.glob('*-analysis.md')
    analysis_files = [f for f in analysis_files if 'copy' not in f]
    
    results = []
    
    for filepath in sorted(analysis_files):
        repo_name, scores = extract_scores_from_file(filepath)
        if repo_name and scores:
            results.append((repo_name, scores))
    
    # Sort by overall score descending
    results.sort(key=lambda x: x[1]['overall'], reverse=True)
    
    # Generate markdown table
    print("| GitHub Repository | Mento SDK | Broker Contract | Oracle | Swap | Code Quality | Overall Score |")
    print("|------------------|-----------|-----------------|--------|------|--------------|---------------|")
    
    for repo_name, scores in results:
        github_url = f"https://github.com/{repo_name}"
        print(f"| [{repo_name}]({github_url}) | {scores['mento_sdk']:.1f} | {scores['broker']:.1f} | {scores['oracle']:.1f} | {scores['swap']:.1f} | {scores['code_quality']:.1f} | {scores['overall']:.1f} |")

if __name__ == "__main__":
    main()
