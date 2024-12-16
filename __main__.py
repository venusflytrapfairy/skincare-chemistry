# -*- coding: utf-8 -*-
"""SkincareLibrary.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1NW8H9A_ZicMlx_ScMXJmQhszrwGC5Q0a
"""

import pandas as pd
import numpy as np

import random
import requests
class SkincareLibrary:
    def __init__(self):
        # Sample ingredient database
        self.ingredient_db = {
            "Hyaluronic Acid": {
                "function": "Humectant",
                "safety_rating": "Safe",
                "skin_types": ["Dry", "Normal", "Oily", "Sensitive"],
                "compatible_bases": ["Moisturizer", "Serum"],
                "recommended_concentration": "1-2%",
                "natural_sources": ["Aloe Vera Gel", "Cucumber Extract"],
                "environmental_impact": "Low impact, biodegradable",
                "conflicts_with":[],
            },
            "Salicylic Acid": {
                "function": "Exfoliant",
                "safety_rating": "Safe in low concentrations",
                "skin_types": ["Oily", "Acne-Prone"],
                "compatible_bases": ["Serum", "Spot Treatment"],
                "recommended_concentration": "0.5-2%",
                "natural_sources": ["Willow Bark Extract"],
                "environmental_impact": "Moderate; can affect aquatic life if overused",
                "conflicts with": ["Retinol", "Azelaic Acid", "Glycolic Acid", "Lactic Acid"],
            },
            "Vitamin C": {
                "function": "Antioxidant",
                "safety_rating": "Potentially irritating for sensitive skin",
                "skin_types": ["Normal", "Oily", "Dry"],
                "compatible_bases": ["Serum", "Moisturizer"],
                "recommended_concentration": "10-20%",
                "natural_sources": ["Citrus Fruits", "Rosehip"],
                "environmental_impact": "Low impact, generally safe",
                "conflicts_with": ["Retinol"],
            },
            "Niacinamide": {
                "function": "Brightening, Anti-inflammatory",
                "safety_rating": "Safe",
                "skin_types": ["All"],
                "compatible_bases": ["Serum", "Toner"],
                "recommended_concentration": "5-10%",
                "natural_sources": ["Yeast Extract", "Rice Water"],
                "environmental_impact": "Low impact, sustainable production",
                 "conflicts_with": ["Vitamin C"],
            },
            "Retinol": {
                "function": "Cell turnover, Anti-aging",
                "safety_rating": "Use with caution, may cause irritation",
                "skin_types": ["Normal", "Oily", "Dry", "Aging"],
                "compatible_bases": ["Serum", "Moisturizer"],
                "recommended_concentration": "0.1-1%",
                "natural_sources": ["Carrots", "Sweet Potatoes"],
                "environmental_impact": "Moderate; sensitive to degradation",
                "conflicts_with": ["Vitamin C", "Salicylic Acid", "Glycolic Acid", "Lactic Acid", "Caffeine"],
            },
            "Ceramides": {
                "function": "Skin barrier repair",
                "safety_rating": "Safe",
                "skin_types": ["Dry", "Sensitive", "Normal"],
                "compatible_bases": ["Moisturizer"],
                "recommended_concentration": "1-3%",
                "natural_sources": ["Soybeans", "Wheat Germ"],
                "environmental_impact": "Low impact, renewable sources",
                "conflicts_with": [],
            },
            "Glycolic Acid": {
                "function": "Exfoliant",
                "safety_rating": "Safe in low concentrations",
                "skin_types": ["Oily", "Normal", "Acne-Prone"],
                "compatible_bases": ["Serum", "Toner"],
                "recommended_concentration": "5-10%",
                "natural_sources": ["Sugarcane"],
                "environmental_impact": "Moderate; overuse can disrupt ecosystems",
                "conflicts_with": ["Retinol", "Vitamin C", "Salicylic Acid"],
            },
            "Lactic Acid": {
                "function": "Exfoliant, Hydration",
                "safety_rating": "Safe in low concentrations",
                "skin_types": ["Dry", "Sensitive", "Normal"],
                "compatible_bases": ["Moisturizer", "Serum"],
                "recommended_concentration": "5-12%",
                "natural_sources": ["Milk", "Tomatoes"],
                "environmental_impact": "Low impact, biodegradable",
                 "conflicts_with": ["Retinol", "Salicylic Acid"],
            },
            "Benzoyl Peroxide": {
                "function": "Acne treatment",
                "safety_rating": "Safe in regulated use",
                "skin_types": ["Oily", "Acne-Prone"],
                "compatible_bases": ["Spot Treatment", "Cleanser"],
                "recommended_concentration": "2.5-10%",
                "natural_sources": None,
                "environmental_impact": "High; non-biodegradable and water-persistent",
                "conflicts_with": ["Retinol"],
            },
            "Zinc Oxide": {
                "function": "UV protection, Soothing",
                "safety_rating": "Safe",
                "skin_types": ["All"],
                "compatible_bases": ["Sunscreen"],
                "recommended_concentration": "10-25%",
                "natural_sources": None,
                "environmental_impact": "Moderate; reef-safe formulations available",
                "conflicts_with": [],
            },
            "Titanium Dioxide": {
                "function": "UV protection",
                "safety_rating": "Safe",
                "skin_types": ["All"],
                "compatible_bases": ["Sunscreen"],
                "recommended_concentration": "5-25%",
                "natural_sources": None,
                "environmental_impact": "Moderate; reef-safe formulations available",
                "conflicts_with": [],
            },
            "Aloe Vera": {
                "function": "Soothing, Hydrating",
                "safety_rating": "Safe",
                "skin_types": ["All"],
                "compatible_bases": ["Gel", "Moisturizer"],
                "recommended_concentration": "10-100%",
                "natural_sources": ["Aloe Vera Plant"],
                "environmental_impact": "Low impact, highly sustainable",
                "conflicts_with": [],
            },
            "Tea Tree Oil": {
                "function": "Anti-microbial, Anti-inflammatory",
                "safety_rating": "Use with caution, may cause irritation",
                "skin_types": ["Oily", "Acne-Prone"],
                "compatible_bases": ["Spot Treatment", "Cleanser"],
                "recommended_concentration": "1-5%",
                "natural_sources": ["Tea Tree Leaves"],
                "environmental_impact": "Low impact, biodegradable",
                "conflicts_with": [],
            },
            "Peptides": {
                "function": "Anti-aging, Skin repair",
                "safety_rating": "Safe",
                "skin_types": ["All"],
                "compatible_bases": ["Serum", "Moisturizer"],
                "recommended_concentration": "1-5%",
                "natural_sources": ["Collagen Hydrolysate"],
                "environmental_impact": "Low impact, sustainable sources available",
                "conflicts_with": ["Glycolic Acid"],
            },
            "Shea Butter": {
                "function": "Moisturizer",
                "safety_rating": "Safe",
                "skin_types": ["Dry", "Sensitive", "Normal"],
                "compatible_bases": ["Moisturizer", "Lip Balm"],
                "recommended_concentration": "5-100%",
                "natural_sources": ["Shea Tree Nuts"],
                "environmental_impact": "Low impact, renewable resource",
                "conflicts_with": [],
            },
            "Caffeine": {
                "function": "Anti-inflammatory, De-puffing",
                "safety_rating": "Safe",
                "skin_types": ["All"],
                "compatible_bases": ["Eye Cream", "Serum"],
                "recommended_concentration": "0.5-3%",
                "natural_sources": ["Coffee", "Green Tea"],
                "environmental_impact": "Low impact, biodegradable",
                "conflicts_with": ["Retinol"],
            },
            "Squalane": {
                "function": "Moisturizer, Skin barrier repair",
                "safety_rating": "Safe",
                "skin_types": ["All"],
                "compatible_bases": ["Moisturizer", "Oil"],
                "recommended_concentration": "5-100%",
                "natural_sources": ["Olives", "Sugarcane"],
                "environmental_impact": "Low impact, plant-derived options preferred",
                "conflicts_with":[],
            },
            "Kojic Acid": {
                "function": "Skin brightening",
                "safety_rating": "Safe in low concentrations",
                "skin_types": ["Normal", "Oily", "Dry"],
                "compatible_bases": ["Serum", "Cream"],
                "recommended_concentration": "1-4%",
                "natural_sources": ["Fermented Rice"],
                "environmental_impact": "Low impact, biodegradable",
                "conflicts_with": [],
            },
            "Azelaic Acid": {
                "function": "Anti-inflammatory, Brightening",
                "safety_rating": "Safe",
                "skin_types": ["Sensitive", "Oily", "Acne-Prone"],
                "compatible_bases": ["Serum", "Cream"],
                "recommended_concentration": "10-20%",
                "natural_sources": ["Barley", "Wheat"],
                "environmental_impact": "Low impact, biodegradable",
                "conflicts_with": ["Salicylic Acid"],
            },
             "Arbutin": {
    "function": "Skin brightening",
    "safety_rating": "Safe",
    "skin_types": ["All"],
    "compatible_bases": ["Serum", "Cream"],
    "recommended_concentration": "2-5%",
    "natural_sources": ["Bearberry"],
    "environmental_impact": "Low impact, biodegradable",
    "conflicts_with": [],
},
"Allantoin": {
    "function": "Soothing, Skin repair",
    "safety_rating": "Safe",
    "skin_types": ["Sensitive", "Dry", "Normal"],
    "compatible_bases": ["Cream", "Ointment"],
    "recommended_concentration": "0.5-2%",
    "natural_sources": ["Comfrey Root"],
    "environmental_impact": "Low impact, biodegradable",
    "conflicts_with": [],
}


            # Add similar structures for other ingredients
        }



    def analyze_ingredient(self, ingredient):
            """
            Analyzes a skincare ingredient.
            Args:
            - ingredient (str): Name of the ingredient to analyze.

            Returns:
            - dict: Information about the ingredient.
            """
            return self.ingredient_db.get(ingredient, "Ingredient not found in the database.")

    def recommend_routine(self, skin_type, concerns):
          """
          Recommends a simple skincare routine based on skin type and concerns.
          Args:
          - skin_type (str): User's skin type.
          - concerns (list): List of skin concerns (e.g., "acne", "dryness").

          Returns:
          - list: Suggested products or ingredients.
          """
          recommendations = []
          if "dryness" in concerns:
              recommendations.append("Use products with Hyaluronic Acid or Ceramides.")
          if "acne" in concerns and skin_type in ["Oily", "Acne-Prone"]:
              recommendations.append("Try Salicylic Acid or Niacinamide products.")
          if "anti-aging" in concerns:
              recommendations.append("Consider Retinol and Vitamin C serums.")
          return recommendations if recommendations else ["No specific recommendations found."]

    def create_formulation(self, base):
        """
        Recommends a formulation based on the specified base product.
        Args:
        - base (str): Base product (e.g., "Moisturizer", "Serum").

        Returns:
        - dict: Recommended formulation with suggested active ingredients.
        """
        recommended_ingredients = [
            ing for ing, details in self.ingredient_db.items() if base in details["compatible_bases"]
        ]

        if not recommended_ingredients:
            return f"No recommended active ingredients for the base '{base}'."

        formulation = {
            "Base": base,
            "Active Ingredients": recommended_ingredients,
        }

        return formulation

    def check_conflicts(self, actives):
          """
          Checks for conflicts between active ingredients.
          Args:
          - actives (list): List of active ingredients.

          Returns:
          - dict: Conflicts and safe combinations.
          """
          conflicts = {}
          safe_combinations = []

          # Iterate through the active ingredients
          for i, ingredient in enumerate(actives):
              if ingredient not in self.ingredient_db:
                  conflicts[ingredient] = "Ingredient not found in the database."
                  continue

              # Get the conflicts for the current ingredient
              ingredient_conflicts = self.ingredient_db[ingredient]["conflicts_with"]

              # Check if any of the other ingredients in the list conflict with the current one
              for j in range(i + 1, len(actives)):
                  other_ingredient = actives[j]
                  if other_ingredient in ingredient_conflicts:
                      if ingredient not in conflicts:
                          conflicts[ingredient] = []
                      conflicts[ingredient].append(other_ingredient)

                      if other_ingredient not in conflicts:
                          conflicts[other_ingredient] = []
                      conflicts[other_ingredient].append(ingredient)

          # Add safe combinations (if no conflicts are found)
          if not conflicts:
              safe_combinations = [f"{actives[i]} and {actives[j]}" for i in range(len(actives)) for j in range(i + 1, len(actives))]

          return {
              "conflicts": conflicts,
              "safe_combinations": safe_combinations,
          }

    def get_diy_recipe(self, base):
        """
        Provides a DIY recipe with natural sources for a specified base product.
        Args:
        - base (str): Base product (e.g., "Moisturizer", "Serum").

        Returns:
        - str: DIY recipe.
        """
        suitable_ingredients = [
            (ing, details["natural_sources"]) for ing, details in self.ingredient_db.items()
            if base in details["compatible_bases"]
        ]

        if not suitable_ingredients:
            return f"No DIY recipes available for the base '{base}'."

        # Randomly pick one ingredient for DIY purposes
        ingredient, sources = random.choice(suitable_ingredients)
        return f"For a DIY {base}, use natural sources of {ingredient}: {', '.join(sources)}."



    def get_environmental_impact(self, ingredient):
       # Convert ingredient to lowercase to allow case-insensitive search
          ingredient = ingredient.lower()

          # Check if the ingredient is in the database
          if ingredient in self.ingredient_db:
              return self.ingredient_db[ingredient]['environmental_impact']
          else:
              return "Ingredient not available in the database."


    def check_product_compatibility(self, product_ingredients, skin_type):
        """
        Checks product compatibility with a given skin type.
        Args:
        - product_ingredients (list): List of ingredients in the product.
        - skin_type (str): User's skin type.

        Returns:
        - dict: Compatible and incompatible ingredients.
        """
        compatible = []
        incompatible = []
        for ingredient in product_ingredients:
            if ingredient in self.ingredient_db:
                if skin_type in self.ingredient_db[ingredient]["skin_types"]:
                    compatible.append(ingredient)
                else:
                    incompatible.append(ingredient)
        return {"compatible": compatible, "incompatible": incompatible}

    def get_cosmetic_trends(self):
        """
        Fetches recent cosmetic trends (example API integration).
        Note: Replace the placeholder API with a real one for production.
        """
        try:
            # Example of API call (Replace with actual API endpoint)
            response = requests.get("https://example.com/api/cosmetic-trends")
            if response.status_code == 200:
                return response.json()
            else:
                return {"error": "Failed to fetch trends. Check API endpoint."}
        except Exception as e:
            return {"error": str(e)}













skincare = SkincareLibrary()

# Deploy and Test the Library
if __name__ == "__main__":
    # Initialize the library
    skincare = SkincareLibrary()

    # Example: Ingredient Analysis
    print("Ingredient Analysis:")
    print(skincare.analyze_ingredient("Hyaluronic Acid"))

    # Example: Skincare Routine Recommendation
    print("\nRoutine Recommendation:")
    print(skincare.recommend_routine("Oily", ["acne", "anti-aging"]))

    print(skincare.check_conflicts(["Hyaluronic Acid", "Vitamin C", "Glycolic Acid"]))



import unittest

class TestSkincareLibrary(unittest.TestCase):
    def setUp(self):
        """Set up a fresh instance of the SkincareLibrary for each test."""
        self.library = SkincareLibrary()

    def test_analyze_ingredient_valid(self):
        """Test that analyze_ingredient returns correct details for a known ingredient."""
        result = self.library.analyze_ingredient("Hyaluronic Acid")
        self.assertEqual(result['function'], "Humectant")
        self.assertIn("Dry", result['skin_types'])

    def test_analyze_ingredient_invalid(self):
        """Test that analyze_ingredient handles unknown ingredients gracefully."""
        result = self.library.analyze_ingredient("Unknown Ingredient")
        self.assertEqual(result, "Ingredient not found in the database.")

    def test_recommend_routine(self):
        """Test that recommend_routine provides correct recommendations."""
        recommendations = self.library.recommend_routine("Dry", ["dryness"])
        self.assertTrue(len(recommendations) > 0)
        self.assertIn("Hyaluronic Acid", recommendations)



# Run the tests
unittest.main(argv=[''], verbosity=2, exit=False)