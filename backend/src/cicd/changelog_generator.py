class ChangelogGenerator:
    def generate(self, commits: list[str]) -> str:
        features = []
        fixes = []
        has_breaking = False
        
        for commit in commits:
            if "BREAKING CHANGE" in commit:
                has_breaking = True
                
            if commit.startswith("feat:"):
                features.append(commit.replace("feat:", "").strip())
            elif commit.startswith("fix:"):
                fixes.append(commit.replace("fix:", "").strip())
            # chore: y ci: se ignoran intencionalmente
        
        if not features and not fixes and not has_breaking:
            return "No public changes to report."
            
        version_bump = "MAJOR (v2.0.0)" if has_breaking else "MINOR (v1.5.0)"
        
        md = f"# Changelog - {version_bump}\n\n"
        if features:
            md += "## Nuevas Caracteristicas\n"
            for f in features:
                md += f"- {f}\n"
        if fixes:
            md += "\n## Correcciones de Errores\n"
            for f in fixes:
                md += f"- {f}\n"
                
        return md

if __name__ == "__main__":
    generator = ChangelogGenerator()
    
    # Prueba 1: Commits mixtos
    commits_week_1 = [
        "feat: anadir endpoint de clima GraphQL",
        "fix: resolver timeout en la base de datos MonetDB",
        "chore: actualizar dependencias npm",
        "ci: arreglar pipeline de GitHub Actions"
    ]
    print("--- CHANGELOG SEMANA 1 ---")
    print(generator.generate(commits_week_1))
    
    # Prueba 2: Solo ruido (no debe generar)
    commits_week_2 = [
        "chore: refactorizar carpeta de utils",
        "ci: nuevo linting"
    ]
    print("\n--- CHANGELOG SEMANA 2 ---")
    print(generator.generate(commits_week_2))
