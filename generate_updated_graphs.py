import os
import matplotlib.pyplot as plt


OUTPUT_DIR = os.path.join('results', 'individual_graphs')


def ensure_output_dir() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)


def save_fig(path: str) -> None:
    plt.tight_layout()
    plt.savefig(path, dpi=200)
    plt.close()


def update_fasterkan_vs_cnn(uji_mpe_improved: float = 3.40) -> None:
    """Graph 2: FasterKAN vs CNN performance (left: positioning error)."""
    plt.figure(figsize=(6, 4))
    models = ['FasterKAN (Paper)', 'FasterKAN (Improved)', 'CNN']
    values = [3.56, uji_mpe_improved, 8.95]
    colors = ['#6baed6', '#31a354', '#fd8d3c']
    plt.bar(models, values, color=colors)
    plt.ylabel('Mean Position Error (m)')
    plt.title('UJI Positioning Error: FasterKAN vs CNN')
    for i, v in enumerate(values):
        plt.text(i, v + 0.05, f"{v:.2f}m", ha='center', va='bottom', fontsize=9)
    save_fig(os.path.join(OUTPUT_DIR, '2_fasterkan_comparison.png'))


def update_improvement_percentage(
    floor_building_paper: float = 99.00,
    floor_building_ours: float = 99.41,
    space_id_paper: float = 71.00,
    space_id_ours: float = 72.98,
    mpe_paper: float = 3.56,
    mpe_ours: float = 3.40,
) -> None:
    """Graph 3: Improvement percentage/deviation vs paper."""
    plt.figure(figsize=(6, 4))
    categories = ['Floor&Building (+%)', 'Space ID (+%)', 'MPE (−m)']
    improvements = [
        floor_building_ours - floor_building_paper,
        space_id_ours - space_id_paper,
        mpe_paper - mpe_ours,
    ]
    colors = ['#3182bd', '#31a354', '#756bb1']
    plt.bar(categories, improvements, color=colors)
    plt.axhline(0, color='black', linewidth=0.8)
    for i, v in enumerate(improvements):
        suffix = '%' if i < 2 else 'm'
        plt.text(i, v + (0.02 if i < 2 else 0.01), f"{v:.2f}{suffix}", ha='center', va='bottom', fontsize=9)
    plt.title('Improvements over Paper (UJI)')
    save_fig(os.path.join(OUTPUT_DIR, '3_improvement_percentage.png'))


def update_floor_building_accuracy(acc: float = 99.41) -> None:
    """Graph 4: Floor & Building classification accuracy (single bar for our model)."""
    plt.figure(figsize=(5, 4))
    plt.bar(['FasterKAN (Improved)'], [acc], color='#31a354')
    plt.ylim(0, 100)
    plt.ylabel('Accuracy (%)')
    plt.title('Floor & Building Classification (UJI)')
    plt.text(0, acc + 0.3, f"{acc:.2f}%", ha='center', va='bottom', fontsize=9)
    save_fig(os.path.join(OUTPUT_DIR, '4_floor_building_classification.png'))


def update_space_id_accuracy(acc: float = 72.98) -> None:
    """Graph 5: Space ID classification accuracy (single bar for our model)."""
    plt.figure(figsize=(5, 4))
    plt.bar(['FasterKAN (Improved)'], [acc], color='#31a354')
    plt.ylim(0, 100)
    plt.ylabel('Accuracy (%)')
    plt.title('Space ID Classification (UJI)')
    plt.text(0, acc + 0.3, f"{acc:.2f}%", ha='center', va='bottom', fontsize=9)
    save_fig(os.path.join(OUTPUT_DIR, '5_space_id_classification.png'))


def main() -> None:
    ensure_output_dir()
    update_fasterkan_vs_cnn(3.40)
    update_improvement_percentage(99.00, 99.41, 71.00, 72.98, 3.56, 3.40)
    update_floor_building_accuracy(99.41)
    update_space_id_accuracy(72.98)


if __name__ == '__main__':
    main()


