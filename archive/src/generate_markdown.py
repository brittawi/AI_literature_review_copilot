def generate_markdown_report(df, claims_df, themes, output_path="outputs/report.md"):
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("# Literature Review Report\n\n")

        # Top papers
        f.write("## Top Papers\n")
        top = df.head(5)

        for _, row in top.iterrows():
            f.write(f"- {row['title']} (Score: {row.get('total_score', 'N/A')})\n")

        f.write("\n")
        
        # most recent papers
        f.write("## Most recent papers\n")
        top_recent = df.sort_values(by="year", ascending=False).head(5)

        for _, row in top_recent.iterrows():
            f.write(f"- {row['title']} ({row['year']})\n")

        f.write("\n")
        
        # highest cited papers
        if "citationCount" in df.columns:
            f.write("## Highest cited papers\n")
            top_cited = df.sort_values(by="citationCount", ascending=False).head(5)

            for _, row in top_cited.iterrows():
                f.write(f"- {row['title']} ({row['citationCount']} citations)\n")

            f.write("\n")

        # Themes
        f.write("## Key Themes\n")

        for t in themes.get("themes", []):
            f.write(f"### {t['theme']}\n")
            for c in t["claims"]:
                f.write(f"- {c}\n")
            f.write("\n")

        # Claims table (short)
        f.write("## Sample Claims\n")

        sample = claims_df.head(10)

        for _, row in sample.iterrows():
            f.write(f"- {row['claim']} (Source: {row['paper']})\n")

        f.write("\n")
        # Notes?
        f.write("## Notes\n")
        
        # Summaries
        f.write("## Summaries\n")
        for _, row in df.iterrows():
            f.write(f"### {row['title']}\n")
            f.write(f"{row['summary']}\n")
            f.write("\n")
        
        f.write("- Generated using AI-assisted literature copilot\n")